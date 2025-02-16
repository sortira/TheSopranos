import streamlit as st
import pyttsx3
def app():
    st.title('Text to Speech')
    
    st.write('Enter text to convert to speech.')
    
    # Text input
    text_input = st.text_area("Enter text:")
    
    if st.button('Convert to Speech'):
        engine = pyttsx3.init()
        engine.setProperty("rate", 130)
        engine.say(text_input)
        engine.runAndWait()