import streamlit as st
import cv2
import numpy as np
import base64
import os
import urllib.request

def download_yolo_files():
    yolo_files = {
        "yolov3.weights": "https://pjreddie.com/media/files/yolov3.weights",
        "yolov3.cfg": "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg",
        "coco.names": "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"
    }
    
    for file_name, url in yolo_files.items():
        if not os.path.exists(file_name):
            st.info(f"Downloading {file_name}...")
            urllib.request.urlretrieve(url, file_name)
            st.success(f"Downloaded {file_name}")

def play_warning_sound():
    sound_file = "warning.mp3"
    with open(sound_file, "rb") as f:
        st.audio(f, format="audio/mp3", autoplay=True)

def app():
    st.title("Real-Time Object Detection and Depth Estimation")
    
    download_yolo_files()  # Ensure YOLO files are available
    
    use_camera = st.checkbox("Use Camera", value=True)
    frame_placeholder = st.empty()
    play_pause_button = st.button("Pause")
    is_playing = True if use_camera else False

    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")  # Load YOLO model
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    
    # Load COCO names
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    
    cap = cv2.VideoCapture(0)   
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
        return
    
    depth_threshold = 100  # Define depth warning threshold
    
    while True:
        if use_camera and is_playing:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to grab frame.")
                break
            
            height, width, _ = frame.shape
            blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)
            
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        center_x, center_y, w, h = (detection[0:4] * np.array([width, height, width, height])).astype(int)
                        x, y = int(center_x - w / 2), int(center_y - h / 2)
                        
                        # Simulated depth estimation
                        depth = 5000 / (w * h)  # Simple estimation
                        
                        color = (0, 255, 0) if depth > depth_threshold else (0, 0, 255)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                        label = f"{classes[class_id]}: {depth:.2f} cm"
                        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                        
                        if depth < depth_threshold:
                            play_warning_sound()
            
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(rgb_frame, channels="RGB", use_column_width=True)
            
            if play_pause_button:
                is_playing = not is_playing
                play_pause_button.text("Resume" if not is_playing else "Pause")
        else:
            frame_placeholder.text("Camera is off. Please check the checkbox to turn on.")
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    app()
