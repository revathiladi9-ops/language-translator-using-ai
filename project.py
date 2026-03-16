import streamlit as st
from googletrans import Translator

# Page title
st.title("🌍 Simple Language Translator")

translator = Translator()

# Text input
text = st.text_area("Enter text to translate")

# Language selection
languages = {
 "English": "en",
 "Hindi": "hi",
"Spanish": "es",
 "French": "fr",
 "German": "de",
 "Chinese": "zh-cn",
 "Japanese": "ja"
}

target_lang = st.selectbox("Select target language", list(languages.keys()))

# Translate button
if st.button("Translate"):
 if text:
     translated = translator.translate(text, dest=languages[target_lang])
 st.success("translated Text:")
 st.write(translated.text)
else:
 st.warning("Please enter some text.")