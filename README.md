# **Real-Time Face Recognition System**

A complete real-time face detection and recognition system built using **Python**, **OpenCV (contrib)**, and the **LBPH Face Recognizer**.
This project allows you to collect face samples, train a recognition model, and perform real-time face recognition through your webcam.

---

## 🚀 Features

* Real-time face detection (Haar Cascade)
* Real-time face recognition using LBPH
* Dataset auto-creation per user
* Train multiple users
* Clean code structure
* No GPU required

---

## 📁 Project Structure

```
Real-time Face Recognition/
│── collect_dataset.py
│── train_recognizer.py
│── recognize.py
│── README.md
│── .gitignore
│
├── haarcascades/
│   └── haarcascade_frontalface_default.xml
│
├── data/          # auto-created; ignored in Git
└── models/        # auto-created; ignored in Git
```

---

# ⚙️ Installation & Setup

### **1. Create Virtual Environment**

Recommended: create venv **outside** your project folder:

```
py -3.11 -m venv face-rec-venv
```

Activate it:

```
.\face-rec-venv\Scripts\Activate.ps1
```

---

### **2. Install Required Packages**

```
pip install numpy==2.2.6 opencv-contrib-python==4.12.0.88
```

---

### **3. Download Haar Cascade**

Place this file inside the `haarcascades/` folder:

* `haarcascade_frontalface_default.xml`

(You can download it from OpenCV GitHub or I can give you a copy.)

---

# 🏃 How to Run the Project (ALL Commands)

## ✅ **Step 1 — Collect Dataset**

Collect 80 images for each user:

```
python collect_dataset.py --name Darshan --id 1 --samples 80
```

Example for another user:

```
python collect_dataset.py --name Alice --id 2 --samples 80
```

---

## ✅ **Step 2 — Train the Model**

This will train the LBPH recognizer and save the model:

```
python train_recognizer.py
```

This generates:

```
models/
    face_recognizer.xml
    labels.json
```

---

## ✅ **Step 3 — Run Real-Time Face Recognition**

Start webcam recognition:

```
python recognize.py
```

Press **Q** to quit.

---

# 📝 .gitignore (Recommended)

```
venv/
__pycache__/
*.pyc
*.pyd
data/
models/
```

---

# 💡 Notes

* Use **OpenCV-Contrib**, NOT the normal opencv-python.
* Make sure your face is well-lit when collecting samples.
* Keep your venv OUTSIDE the project to avoid GitHub issues.

---

# 🛠 Future Enhancements

* Add attendance/entry logging
* Add GUI
* Add deep-learning model (FaceNet / Dlib / Mediapipe)
* Add face anti-spoofing

---

# 👤 Author

**Darshan Naik**
Engineering Final-Year Project — Real-Time Face Recognition

