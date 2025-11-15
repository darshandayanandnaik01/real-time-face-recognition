import cv2
import os
import argparse

def create_user_folder(user_id, name):
    folder = os.path.join("data", f"{user_id}_{name}")
    os.makedirs(folder, exist_ok=True)
    return folder

def collect_samples(name, user_id, samples=80):
    face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)

    folder_path = create_user_folder(user_id, name)
    count = 0

    print("[INFO] Collecting face samples. Look at the camera...")

    while count < samples:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y+h, x:x+w]
            cv2.imwrite(f"{folder_path}/{count}.png", face_img)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Samples: {count}/{samples}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Collecting Samples", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if count >= samples:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Sample collection finished.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--id", required=True)
    parser.add_argument("--samples", default=80, type=int)
    args = parser.parse_args()

    collect_samples(args.name, args.id, args.samples)
