# Abler: AI-Powered Accessibility

Abler is an advanced AI-driven accessibility assistant designed to empower individuals with visual, auditory, and mobility impairments. By leveraging state-of-the-art machine learning techniques, Abler provides real-time object detection, depth estimation, gesture recognition, and speech processing, ensuring seamless interaction with the environment.

---

## 🔧 Features & Architecture
Abler is built on a modular, end-to-end architecture with robust ML model training, optimization, and real-time inference. The system is divided into:

### **1. Data Collection & Preprocessing**
- **Sensor Inputs:** Camera (image/video), Microphone (audio)
- **Databases:**
  - Image/Video Datasets
  - Audio Datasets
  - Gesture & Human Activity Recognition (HAR) Datasets
  - User Preferences & Labeling Data
  - **MLflow/DVC** for model versioning
- **Preprocessing Techniques:**
  - Normalization & Rescaling
  - Augmentations: Rotations, Color Jitter, Mixup
  - Speech: Chunking, Noise Filtering

---

### **2. ML Model Training Pipeline**
#### 🖐 Gesture Recognition
- **Model:** YOLOv8x-tuned-hand-gestures
- **Training Strategy:** Fine-tuned on **8,000+ gestures** using **Curriculum Learning** and **Knowledge Distillation**

#### 🎯 Object & Depth Detection
- **Object Detection:**
  - **YOLOv8** for rapid obstacle detection
  - **DETR (ResNet-50 Backbone)** trained on COCO 2017 (118K images) for precise localization
- **Depth Estimation:**
  - Uses **Apple DepthPro-hf** for real-time depth heatmaps
  - Fuses object detection with depth data for **spatial awareness**

#### 🏃 Human Activity Recognition (HAR)
- **Model:** 3D CNN / I3D / Transformer-based
- **Techniques:** Sliding Window Approach for temporal pattern recognition

#### 🎙 Speech Processing
- **Speech-to-Text (STT):**
  - **wav2vec2** (via `SpeechRecognition` API)
  - CMUSphinx as a **fallback** for noisy environments
- **Text-to-Speech (TTS):**
  - **pyttsx3**, Tacotron 2, WaveGlow for natural speech synthesis

---

### **3. Multi-Task Learning & Model Optimization**
- **Shared Backbone:** ConvNeXt, Swin Transformer
- **Fusion Strategy:**
  - Combined Loss Function (Weighted Sum)
  - Parallel Heads for Object, Gesture, Speech Tasks
- **Optimization Techniques:**
  - **Quantization, Pruning, Knowledge Distillation**
  - Export Formats: **ONNX, TFLite, Core ML**

---

### **4. Real-Time Inference Pipeline**
#### 🎥 Sensor Acquisition
- **Continuous Capture** from Camera, Microphone, Gesture Sensors

#### ⚡ On-Device Preprocessing
- **Frame Normalization, Resizing**
- **Audio Chunking & Filtering**

#### 🤖 ML Inference
- Runs **Object Detection, Depth Estimation, Gesture Recognition, HAR** in **parallel**

#### 🧠 Fusion & Decision Making
- Combines multi-modal outputs
- Rule-based or learned fusion for **better accuracy**

#### 🏆 User Interaction
- **TTS (Audio Alerts)**
- **STT (Voice Commands)**
- **Haptic & Visual Feedback**

---

### **5. Mobile Application & Deployment**
#### 📱 Cross-Platform App
- **React Native / Flutter** or **Native (Swift/Kotlin)**
- Integrates ML inference modules
- Local storage for user preferences

#### ☁️ Cloud & Edge Deployment
- **ML-Ops & CI/CD Pipelines**
- Hybrid Inference (Cloud + On-Device)
- **Logging, Analytics, User Feedback**

---

## 🚀 Tech Stack & Libraries
### 📦 Machine Learning
- **PyTorch / TensorFlow**
- **OpenCV** (Image Processing)
- **Transformers (Hugging Face)**
- **ONNX Runtime**
- **SpeechRecognition, pyttsx3, Tacotron 2**

### 📱 Mobile & Web
- **React Native / Flutter**
- **Firebase / SQLite** (Local Storage)
- **FastAPI / Flask** (Backend APIs)

### ☁️ Cloud & Deployment
- **Docker / Kubernetes**
- **AWS Lambda / GCP Functions**
- **DVC / MLflow** (Model Versioning)

---

## 🎯 Future Enhancements
- 🔥 **Personalized AI Recommendations** based on user behavior
- 🌍 **Multi-Language Support** for broader accessibility
- 📡 **Edge AI Processing** for ultra-fast inference
- 🧠 **Adaptive Learning Models** that improve over time

---

## 🏆 Contributing
We welcome contributions from the community! Feel free to **fork, raise issues, or submit PRs** to improve Abler.

---

## 📄 License
See `LICENSE` for details.

---

🚀 **Abler** – Empowering Accessibility with AI! 💡


Developed with ❤️ for the world by Team TheSopranos (but mainly developed for the eXathon competition).

