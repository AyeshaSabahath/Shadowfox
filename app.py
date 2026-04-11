import streamlit as st
from predictor import SmartKeyboard

keyboard = SmartKeyboard("sample_text.txt")

st.title("Smart Autocorrect Keyboard")

sentence = st.text_input("Type your sentence")

if sentence:
    words = sentence.split()

    corrected_words = []
    for word in words:
        corrected = keyboard.autocorrect_word(word)
        corrected_words.append(corrected)

    corrected_sentence = " ".join(corrected_words)

    st.write("Corrected Sentence:")
    st.success(corrected_sentence)

    last_word = corrected_words[-1]
    prediction = keyboard.predict_next_word(last_word)

    st.write("Next Word Prediction:")
    st.info(prediction)