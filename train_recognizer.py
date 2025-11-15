import cv2
import os
import json
import numpy as np

def load_images():
    data_dir = "data"
    faces = []
    labels = []
    label_map = {}

    users = os.listdir(data_dir)
    user_id = 0

    for folder in users:
        full_path = os.path.join(data_dir, folder)
        if not os.path.isdir(full_path):
            continue

        label_map[user_id] = folder

        for img_name in os.listdir(full_path):
            img_path = os.path.join(full_path, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                continue

            faces.append(img)
            labels.append(user_id)

        user_id += 1

    return faces, labels, label_map

def train_model():
    print("[INFO] Loading face data...")
    faces, labels, label_map = load_images()

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(labels))

    os.makedirs("models", exist_ok=True)
    recognizer.save("models/face_recognizer.xml")

    with open("models/labels.json", "w") as f:
        json.dump(label_map, f)

    print("[INFO] Training completed.")
    print("[INFO] Model saved to models/face_recognizer.xml")

if __name__ == "__main__":
    train_model()
