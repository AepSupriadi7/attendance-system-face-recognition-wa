import cv2
import os
import time

# ======================
# INPUT NAMA
# ======================
name = input("Masukkan nama: ")

# ======================
# FOLDER DATASET
# ======================
dataset_path = "dataset"

if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# ======================
# FACE DETECTOR
# ======================
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

# ======================
# CAMERA
# ======================
cap = cv2.VideoCapture(1)

count = 0

# waktu terakhir save
last_capture_time = time.time()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0,255,0),
            2
        )

        current_time = time.time()

        # simpan tiap 0.5 detik
        if current_time - last_capture_time > 0.5:

            face = frame[y:y+h, x:x+w]

            file_name = f"{name}_{count}.jpg"

            cv2.imwrite(
                os.path.join(dataset_path, file_name),
                face
            )

            count += 1

            last_capture_time = current_time

            print(f"Saved {count}")

        cv2.putText(
            frame,
            f"Images: {count}",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

    cv2.imshow("Capture Face", frame)

    # ESC keluar
    if cv2.waitKey(1) == 27:
        break

    # stop setelah 30 gambar
    if count >= 30:
        break

cap.release()
cv2.destroyAllWindows()

print("Dataset selesai!")