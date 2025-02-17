import streamlit as st
import cv2
import pygame

# used to play warning sound
def warn():
    pygame.mixer.init()
    pygame.mixer.music.load("warning.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock.tick(10)


def app():
# Load pre-trained Haar Cascade for face detection (included with OpenCV)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Streamlit title
    st.title("Abler Real Time Object Detection and Depth Estimation")

    # Checkbox to enable or disable camera usage
    use_camera = st.checkbox("Use Camera", value=True)

    # Initialize placeholders for video feed and control buttons
    frame_placeholder = st.empty()
    play_pause_button = st.button("Pause")

    # Create a variable to manage the play/pause state
    is_playing = True if use_camera else False

    # Initialize webcam (0 is the default webcam)
    cap = cv2.VideoCapture(0)

    # Check if webcam is opened
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
    else:
        while True:
            # Check if camera is enabled and the play button is pressed
            if use_camera and is_playing:
                # Capture frame-by-frame
                ret, frame = cap.read()

                # If frame is read correctly, ret will be True
                if not ret:
                    st.error("Failed to grab frame.")
                    break

                # Convert to grayscale for face detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Detect faces
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                # Draw bounding boxes around detected faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Convert the frame to RGB before displaying in Streamlit
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Display the processed frame in Streamlit
                frame_placeholder.image(rgb_frame, channels="RGB",use_column_width=True)

                # If Play/Pause button is pressed, toggle the play state
                if play_pause_button:
                    is_playing = not is_playing
                    play_pause_button.text("Resume" if not is_playing else "Pause")

            else:
                # Display message when webcam feed is not active
                frame_placeholder.text("Camera is off. Please check the checkbox to turn on.")

    # Release the webcam when done
    cap.release()
    cv2.destroyAllWindows()
