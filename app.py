import streamlit as st
from funcs import home, about, pipeline, object_detection, gesture_detection, speech_to_text, text_to_speech, accessdb
# Set page configuration
st.set_page_config(page_title="AI App", layout="wide", initial_sidebar_state="collapsed")

# Sidebar as a collapsible hamburger menu
with st.sidebar:
    st.markdown("Navigation")  # Hamburger icon
    with st.expander("Menu", expanded=True):  # Expanding menu
        if st.button("🏠 Home"):
            st.session_state.page = "Home"
        if st.button("ℹ️ About Us"):
            st.session_state.page = "About Us"
        if st.button("🔗 Pipeline"):
            st.session_state.page = "Pipeline"
        if st.button("🎯 Object Detection"):
            st.session_state.page = "Object Detection"
        if st.button("✋ Gesture Detection"):
            st.session_state.page = "Gesture Detection"
        if st.button("🗣️ Speech to Text"):
            st.session_state.page = "Speech to Text"
        if st.button("🔊 Text to Speech"):
            st.session_state.page = "Text to Speech"
        if st.button("Accessibility Database"):
            st.session_state.page = "Accessibility Database"

# Ensure session state is initialized
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Load the selected page
if st.session_state.page == "Home":
    home.app()
elif st.session_state.page == "About Us":
    about.app()
elif st.session_state.page == "Pipeline":
    pipeline.app()
elif st.session_state.page == "Object Detection":
    object_detection.app()
elif st.session_state.page == "Gesture Detection":
    gesture_detection.app()
elif st.session_state.page == "Speech to Text":
    speech_to_text.app()
elif st.session_state.page == "Text to Speech":
    text_to_speech.app()
elif st.session_state.page == "Accessibility Database":
    accessdb.app()