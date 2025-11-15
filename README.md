<h1 align="center">Real-Time Face Recognition System</h1>
<p align="center">A Python & OpenCV-based real-time face detection and recognition system using LBPH.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue">
  <img src="https://img.shields.io/badge/OpenCV-Contrib-green">
  <img src="https://img.shields.io/badge/Face%20Recognition-LBPH-orange">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen">
</p>

---

## 📖 Overview

This project implements a **real-time face recognition system** using:

- **OpenCV Haar Cascade** for face detection  
- **LBPH (Local Binary Patterns Histogram)** for face recognition  
- **Python** for dataset creation, model training, and live recognition  

It supports **multiple users**, automatic dataset generation, and real-time predictions using a webcam.

---

## 📁 Project Structure

Real-time Face Recognition/
│── collect_dataset.py # Capture user face images
│── train_recognizer.py # Train LBPH model
│── recognize.py # Live recognition using webcam
│── README.md
│── .gitignore
│
├── haarcascades/
│ └── haarcascade_frontalface_default.xml
│
├── data/ # Auto-created user datasets
└── models/ # Trained model + label mapping

yaml
Copy code

---

## 🚀 Features

- ✔ Real-time face detection  
- ✔ Real-time face recognition  
- ✔ Supports multiple users  
- ✔ Lightweight and fast (no GPU required)  
- ✔ Simple 3-step workflow  
- ✔ Clean, modular Python scripts  

---

# ⚙️ Installation & Setup

### **1. Create and activate a virtual environment**
Recommended: outside the project folder.

```powershell
py -3.11 -m venv face-rec-venv
.\face-rec-venv\Scripts\Activate.ps1
2. Install required dependencies
powershell
Copy code
pip install numpy==2.2.6 opencv-contrib-python==4.12.0.88
3. Ensure Haar Cascade file exists
Place the file inside:

bash
Copy code
haarcascades/haarcascade_frontalface_default.xml
▶️ How to Run the Project
✅ Step 1 — Collect Dataset
Capture images using your webcam:

powershell
Copy code
python collect_dataset.py --name Darshan --id 1 --samples 80
Example for another user:

powershell
Copy code
python collect_dataset.py --name Alice --id 2 --samples 80
✅ Step 2 — Train the Model
powershell
Copy code
python train_recognizer.py
This creates:

pgsql
Copy code
models/
    face_recognizer.xml
    labels.json
✅ Step 3 — Run Real-Time Recognition
powershell
Copy code
python recognize.py
Press Q to quit.

📝 .gitignore (Recommended)
markdown
Copy code
venv/
__pycache__/
*.pyc
*.pyd
data/
models/
📌 Example Output (Optional - You can add later)
You can add screenshots or a GIF here:

bash
Copy code
# Example:
# ┌─────────────────────────────┐
# │   [ Darshan ]               │
# │   Face detected with box    │
# │   Confidence: 72%           │
# └─────────────────────────────┘
🛠 Future Improvements
Add attendance logging system

Add GUI (Tkinter or PyQT)

Use deep learning (FaceNet / Dlib / Mediapipe)

Add face anti-spoofing

Add model accuracy report

👤 Author
Darshan Naik
Engineering Final-Year Project
Real-Time Face Recognition System
