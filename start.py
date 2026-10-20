#!/usr/bin/env python3
"""
One-command launcher for the offline translator.

    python start.py

First run (needs internet once): downloads the translation engine and the
NLLB-200 model next to this file. Every later run skips what is already
there, works with no internet, and just starts the local page.

Needs only Python 3.8+. No pip packages, no Node.

    python start.py --port 9000 --no-browser
    python start.py --skip-download        # never touch the network
"""

import argparse
import http.server
import sys
import urllib.error
import urllib.request
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
JSDELIVR = "https://cdn.jsdelivr.net/npm/@xenova/transformers@2.17.2/dist/"
HF = "https://huggingface.co/Xenova/nllb-200-distilled-600M/resolve/main/"
MODEL_DIR = "models/Xenova/nllb-200-distilled-600M/"

# (url, local path, required)
FILES = [
    (JSDELIVR + "transformers.min.js", "lib/transformers.min.js", True),
    (JSDELIVR + "ort-wasm.wasm", "lib/ort-wasm.wasm", True),
    (JSDELIVR + "ort-wasm-simd.wasm", "lib/ort-wasm-simd.wasm", True),
    (JSDELIVR + "ort-wasm-threaded.wasm", "lib/ort-wasm-threaded.wasm", False),
    (JSDELIVR + "ort-wasm-simd-threaded.wasm", "lib/ort-wasm-simd-threaded.wasm", False),
    (HF + "config.json", MODEL_DIR + "config.json", True),
    (HF + "generation_config.json", MODEL_DIR + "generation_config.json", True),
    (HF + "tokenizer.json", MODEL_DIR + "tokenizer.json", True),
    (HF + "tokenizer_config.json", MODEL_DIR + "tokenizer_config.json", True),
    (HF + "special_tokens_map.json", MODEL_DIR + "special_tokens_map.json", True),
    (HF + "onnx/encoder_model_quantized.onnx", MODEL_DIR + "onnx/encoder_model_quantized.onnx", True),
    (HF + "onnx/decoder_model_merged_quantized.onnx", MODEL_DIR + "onnx/decoder_model_merged_quantized.onnx", True),
]


def download(url, rel, required):
    dest = ROOT / rel
    if dest.exists() and dest.stat().st_size > 0:
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    part = dest.with_name(dest.name + ".part")
    req = urllib.request.Request(url, headers={"User-Agent": "offline-translator-setup"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp, open(part, "wb") as out:
            total = int(resp.headers.get("Content-Length") or 0)
            done = 0
            while True:
                chunk = resp.read(1 << 20)
                if not chunk:
                    break
                out.write(chunk)
                done += len(chunk)
                if total:
                    sys.stdout.write(f"\r  {rel}  {done / 1e6:7.1f} / {total / 1e6:.1f} MB")
                else:
                    sys.stdout.write(f"\r  {rel}  {done / 1e6:7.1f} MB")
                sys.stdout.flush()
        part.replace(dest)
        print()
        return True
    except (urllib.error.URLError, OSError) as exc:
        print()
        if part.exists():
            part.unlink()
        if required:
            print(f"  Failed: {rel}\n  {exc}")
        else:
            print(f"  Skipped optional file {rel}")
        return not required


def ensure_files():
    missing = [f for f in FILES if not (ROOT / f[1]).exists()]
    if missing:
        print("Downloading the translation engine and model (one time, roughly 1 GB)...")
    ok = True
    for url, rel, required in FILES:
        ok = download(url, rel, required) and ok
    return ok


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".js": "text/javascript",
        ".mjs": "text/javascript",
        ".wasm": "application/wasm",
        ".json": "application/json",
        ".html": "text/html; charset=utf-8",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, *args):  # no request logging
        pass

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()

    def _host_ok(self):
        host = self.headers.get("Host", "").rsplit(":", 1)[0].lower()
        return host in ("127.0.0.1", "localhost")

    def do_GET(self):
        if not self._host_ok():
            return self.send_error(403)
        super().do_GET()

    def do_HEAD(self):
        if not self._host_ok():
            return self.send_error(403)
        super().do_HEAD()

    def list_directory(self, path):
        self.send_error(404)
        return None


def main():
    parser = argparse.ArgumentParser(description="Offline translator launcher")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--skip-download", action="store_true")
    args = parser.parse_args()

    if not (ROOT / "index.html").exists():
        sys.exit("index.html must be in the same folder as start.py")

    if not args.skip_download and not ensure_files():
        print("\nSome files could not be downloaded. Connect to the internet and run again;")
        print("finished files are kept, so it resumes from where it stopped.")
        sys.exit(1)

    http.server.ThreadingHTTPServer.daemon_threads = True
    server = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{args.port}"
    print(f"\nOffline translator running at {url}  (Ctrl+C to stop)")
    if not args.no_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
