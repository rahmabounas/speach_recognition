import streamlit as st
import speech_recognition as sr
import os
from datetime import datetime

# Available APIs mapping
API_OPTIONS = {
    "Google Web Speech API": "google",
    "Sphinx (offline)": "sphinx",
    # You can configure these if you have API keys:
    # "Wit.ai": "wit",
    # "Microsoft Bing Voice Recognition": "bing",
    # "IBM Speech to Text": "ibm",
}

# Available languages (add more as needed)
LANGUAGE_OPTIONS = {
    "English (US)": "en-US",
    "French": "fr-FR",
    "Spanish": "es-ES",
    "Arabic (Saudi Arabia)": "ar-SA",
}

# Initialize recognizer
r = sr.Recognizer()

def transcribe_speech(api_choice="google", language="en-US"):
    with sr.Microphone() as source:
        st.info("Speak now... (click Pause to stop)")
        audio_text = r.listen(source, phrase_time_limit=10)
        st.info("Transcribing...")

    try:
        if api_choice == "google":
            return r.recognize_google(audio_text, language=language)
        elif api_choice == "sphinx":
            return r.recognize_sphinx(audio_text, language=language)
        else:
            return "API not yet implemented or configured."
    except sr.UnknownValueError:
        return "Speech was unintelligible. Please try again."
    except sr.RequestError as e:
        return f"Could not request results; {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def save_transcription(text):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"transcription_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    st.success(f"Transcription saved as {filename}")

def main():
    st.title("🔊 Speech Recognition App")
    st.write("Select your options and click **Start Recording**.")

    # API and language selection
    api_choice = st.selectbox("Choose Speech Recognition API", list(API_OPTIONS.keys()))
    lang_choice = st.selectbox("Choose Language", list(LANGUAGE_OPTIONS.keys()))

    # Controls
    if "paused" not in st.session_state:
        st.session_state.paused = False
    if "transcription" not in st.session_state:
        st.session_state.transcription = ""

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start Recording"):
            if not st.session_state.paused:
                result = transcribe_speech(API_OPTIONS[api_choice], LANGUAGE_OPTIONS[lang_choice])
                st.session_state.transcription = result
                st.success("Transcription: " + result)
    with col2:
        if st.button("Pause/Resume"):
            st.session_state.paused = not st.session_state.paused
            state = "Paused" if st.session_state.paused else "Resumed"
            st.warning(f"Recognition {state}")

    # Save to file
    if st.session_state.transcription:
        if st.button("Save Transcription"):
            save_transcription(st.session_state.transcription)

if __name__ == "__main__":
    main()
