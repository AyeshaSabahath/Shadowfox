import streamlit as st
from predictor import SmartKeyboard

keyboard = SmartKeyboard("sample_text.txt")

st.set_page_config(page_title="Smart Autocorrect Keyboard")

st.title("Smart Autocorrect Keyboard")

sentence = st.text_input("Type your sentence")

if sentence.strip():
    corrected_words = keyboard.autocorrect_sentence(sentence)
    corrected_sentence = " ".join(corrected_words)

    st.subheader("Corrected Sentence")
    st.success(corrected_sentence)

    last_word = corrected_words[-1]

    suggestions = keyboard.predict_next_words(last_word)

    st.subheader("Next Word Suggestions")

    for suggestion in suggestions:
        st.info(suggestion)