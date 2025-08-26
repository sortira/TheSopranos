import streamlit as st
import streamlit.components.v1 as components

# Must be the very first Streamlit command.
st.set_page_config(page_title="Abler App", layout="wide")

# Inject hidden HTML/JS to capture voice commands via the Web Speech API.
components.html(
    """
    <script>
      // Use the Web Speech API if supported.
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (SpeechRecognition) {
          const recognition = new SpeechRecognition();
          recognition.continuous = true;
          recognition.interimResults = false;
          recognition.lang = "en-US";
          recognition.onresult = function(event) {
              let command = event.results[event.results.length - 1][0].transcript.trim().toLowerCase();
              // Set the command in a hidden input and submit the form.
              document.getElementById("voice-command").value = command;
              document.getElementById("voiceForm").submit();
          };
          recognition.onerror = function(event) {
              console.error("Speech recognition error", event);
          };
          recognition.start();
      } else {
          console.log("Browser does not support Speech Recognition");
      }
    </script>
    <form id="voiceForm" method="GET">
      <input id="voice-command" name="voice_command" type="hidden" value="">
    </form>
    """,
    height=0,
)

# Use st.query_params (a property) to get the voice command.
params = st.query_params
voice_command = params.get("voice_command", [""])[0].lower()

# Fixed mapping of voice keywords to page names.
VOICE_PAGES = {
    "home": "Home",
    "inference": "Real-time Inference",
    "dashboard": "Dashboard",
    "pipeline": "Pipeline Info",
    "speech": "Speech to Text",
    "text": "Text to Speech",
    "about": "About",
    "login": "Login",
    "signup": "Signup"
}

selected_page = None
for key, page_name in VOICE_PAGES.items():
    if key in voice_command:
        selected_page = page_name
        break

# Clear the query parameter if a command was detected.
if voice_command:
    st.set_query_params(voice_command="")

# Import all the page modules.
from funcs import home, dashboard, pipeline, speech_to_text, text_to_speech, about, login, signup, accessdb, realtime_inference

PAGES = {
    "Home": home.app,
    "Real-time Inference": realtime_inference.realtime_inference_app,
    "Dashboard": dashboard.app,
    "Accessibility Ratings": accessdb.app,
    # "Pipeline Info": pipeline.app,
    "Speech to Text": speech_to_text.app,
    "Text to Speech": text_to_speech.app,
    # "About": about.app,
    "Login": login.app,
    "Signup": signup.app,
}

if selected_page is None:
    st.sidebar.title("Abler App Navigation")
    selection = st.sidebar.radio("Select Page", list(PAGES.keys()))
else:
    selection = selected_page
    st.sidebar.title("Abler App Navigation")
    st.sidebar.write(f"Navigated to **{selection}** via voice command.")

page = PAGES[selection]
page()
