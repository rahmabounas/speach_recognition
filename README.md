# 🎙️ Enjoy Speech Recognition App

Welcome to the **Enjoy Speech Recognition App** – a simple and powerful tool for converting speech into text using different recognition engines, including offline support via CMU Sphinx!

🚀 **Live Demo**: [Try the App on Streamlit](https://enjoyspeechrecognition.streamlit.app/)

---

## ✨ Features

- 🎤 Record your voice and convert it into text in real-time.
- 🌐 **Choose your speech recognition engine**:
  - Google Web Speech API (online)
  - CMU Sphinx (offline, works without internet)
- 🌍 Select the language you are speaking (Google only).
- ⏸️ Pause and resume speech recognition as needed.
- 💾 Save your transcribed text into a `.txt` file.
- 📱 Simple and clean user interface using Streamlit.

---

## 🛠️ Requirements

To run this app locally, you need:

```bash
pip install streamlit
pip install SpeechRecognition
pip install pocketsphinx  # For offline recognition with Sphinx
```

---


## 📂 How to Run Locally

```bash
git clone https://github.com/your-username/speech-recognition-app.git
cd speech-recognition-app
streamlit run simple_speach_recog_app.py

```
---
# 📝 Notes

- **CMU Sphinx** does not support language selection and works best with **English (US)**.
- If you're using **Google Speech Recognition**, an **active internet connection** is required.
- For advanced use cases or large vocabulary support, consider integrating with more robust APIs such as:
  - [Wit.ai](https://wit.ai)
  - [Azure Speech Services](https://azure.microsoft.com/en-us/services/cognitive-services/speech-services/)
  - [IBM Watson Speech to Text](https://www.ibm.com/cloud/watson-speech-to-text)

---

# 📄 License

This project is open-source and freely available under the **MIT License**.  
Feel free to use, modify, and share it with proper attribution.

---

# 🙌 Acknowledgements

Special thanks to the developers and maintainers of the following tools and libraries:

- [Streamlit](https://streamlit.io/) – for the interactive web app framework.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – for providing access to multiple speech-to-text engines.
- [CMU Sphinx](https://cmusphinx.github.io/) – for enabling offline speech recognition.




