# OfflineTranslator
# 🌐 OfflineTranslator

<p align="center">
  <strong>Translate languages locally. Keep your text private.</strong>
  <br>
  A browser-based translation application inspired by Google Translate, designed to work offline after its translation models are downloaded.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Mode-Offline-16A34A?style=for-the-badge" alt="Offline mode">
  <img src="https://img.shields.io/badge/Interface-Web-6366F1?style=for-the-badge" alt="Web interface">
</p>

---

## 📸 Preview

<p align="center">
  <img src="screenshots/translator.png" alt="OfflineTranslator interface" width="90%">
</p>

<p align="center">
  <em>A clean, side-by-side translation interface with language selection and text input.</em>
</p>

> To display the preview, save your application screenshot as `screenshots/translator.png` inside the repository. If you use a different path, update the image reference above.

## ✨ Features

- 🌍 **Language Translation** — Translate text between supported languages.
- 🔄 **Language Switching** — Switch the source and target languages.
- 📝 **Simple Text Input** — Enter text directly into the translator.
- 📋 **Copy Translation** — Copy the translated output.
- 🌙 **Dark Interface** — A modern interface inspired by popular translation tools.
- 🔒 **Local Processing** — Translation runs in the browser using locally available models.
- 📡 **Offline Support** — Translate without an internet connection after the required model files have been downloaded.
- ⚡ **Local Startup** — Launch the application using a simple Python command.

## 🧠 How It Works

OfflineTranslator uses a local web interface and translation models to process text.

```text
        ┌─────────────────────────┐
        │   Run python start.py   │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Start Local Application │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Load Translation Models │
        │ First Run: Internet     │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Select Languages & Text │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Translate Locally       │
        │ Offline After Download  │
        └─────────────────────────┘
```

## ⚙️ Requirements

- Python installed on your computer.
- The project dependencies installed.
- An internet connection for the initial translation model download.
- Sufficient disk space for the downloaded models.
- A modern web browser.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd OfflineTranslator
```

Replace `<YOUR_REPOSITORY_URL>` with the actual GitHub repository URL.

### 2. Install Dependencies

If the project contains a `requirements.txt` file, run:

```bash
python -m pip install -r requirements.txt
```

### 3. Start the Application

Run this command from the directory containing `start.py`:

```bash
python start.py
```

### 4. Open the Translator

Follow the local address displayed in the terminal, if the script provides one.

**Important:** Do not open `index.html` directly by double-clicking it. Browsers may block locally loaded translation model files when a page is opened using the `file://` protocol. Start the application through `start.py` instead.

## 📡 Internet and Offline Usage

| Stage | Internet Required? |
|---|---|
| First launch and model download | Yes |
| Downloading additional models | Yes |
| Translation after required models are downloaded | No, if the application and models support offline operation |
| Using a language pair whose model is not downloaded | Potentially yes |

Once the necessary models are available locally, the application is intended to translate text without repeatedly downloading translation data.

## 🔐 Privacy

OfflineTranslator is designed to process translations locally.

- Text can be processed using locally available models.
- Internet access is needed initially to download the required model files.
- After setup, translation can work without an internet connection.

Actual privacy guarantees depend on the implementation and whether any external services are called. Inspect the code to confirm that text is never transmitted externally.

## 🛠️ Troubleshooting

**The translation does not work when opening `index.html` directly**

Run the application from the terminal:

```bash
python start.py
```

**The model fails to download**

Check your internet connection and ensure the computer has enough disk space. Retry the initial setup.

**Translation does not work offline**

Verify that the required model files were downloaded successfully and that the selected language pair is supported by the installed models.

**Python is not recognized**

Install Python and ensure it is available in your system's PATH.

## 🗺️ Future Improvements

- [ ] Support for more languages and language pairs.
- [ ] Improved translation speed.
- [ ] Automatic language detection.
- [ ] Translation history stored locally.
- [ ] Text-to-speech support.
- [ ] Document translation.
- [ ] Desktop application packaging.

## 🤝 Contributing

Suggestions, bug reports, and feature improvements are welcome.

1. Fork the repository.
2. Create a new branch.
3. Implement your changes.
4. Submit a Pull Request.

## 📄 License

No license is specified in this README. Add a `LICENSE` file if you want to define how others may use or distribute the project.

---

<p align="center">
  <strong>🌐 OfflineTranslator</strong>
  <br>
  <em>Your translations, running locally.</em>
</p>
