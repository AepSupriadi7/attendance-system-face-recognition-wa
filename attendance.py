import cv2
import csv
import pywhatkit
import time

from datetime import datetime

# =========================
# LOAD MODEL TRAINING
# =========================
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

# =========================
# FACE DETECTOR
# =========================
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

# =========================
# NAMA SESUAI TRAINING
# =========================
names = {
    0: "Aep Supriadi",
    1: "Luthfi",
    2: "Ainun",
    3: "Prabowo"
}

# =========================
# ABSENSI YANG SUDAH MASUK
# =========================
attendance_taken = set()

# =========================
# NOMOR WHATSAPP ORANG TUA
# =========================
parent_numbers = {
    "Aep Supriadi": "+6285811470900",
    "Luthfi": "+6285811470900",
    "Naura Zainatur Rohimah": "+6283812574412",
    "Siti Sarmanah": "+6283896060187",
    "Prabowo": "+6285811470900"
}

# =========================
# CAMERA
# =========================
cap = cv2.VideoCapture(1)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]

        # =========================
        # PREDICT WAJAH
        # =========================
        id, confidence = recognizer.predict(face)

        # semakin kecil confidence semakin bagus
        if confidence < 50:

            name = names.get(id, "Unknown")

            # =========================
            # ABSENSI SEKALI SAJA
            # =========================
            if name not in attendance_taken:

                now = datetime.now()

                tanggal = now.strftime("%d-%m-%Y")
                jam = now.strftime("%H:%M:%S")

                # =========================
                # SIMPAN CSV
                # =========================
                with open(
                    "attendance.csv",
                    "a",
                    newline=""
                ) as file:

                    writer = csv.writer(file)

                    writer.writerow([
                        name,
                        tanggal,
                        jam
                    ])

                attendance_taken.add(name)

                print(f"{name} berhasil absen")

                # =========================
                # PESAN WHATSAPP
                # =========================
                pesan = f"""
[ SMART ATTENDANCE ]

Nama   : {name}
Status : HADIR
Tanggal: {tanggal}
Jam    : {jam}

Terima kasih.
"""

                nomor_ortu = parent_numbers.get(name)

                if nomor_ortu:

                    time.sleep(2)

                    pywhatkit.sendwhatmsg_instantly(
                        nomor_ortu,
                        pesan,
                        wait_time=15,
                        tab_close=True
                    )

                    print(
                        f"WhatsApp terkirim ke orang tua {name}"
                    )

        else:
            name = "Unknown"

        # =========================
        # TAMPILKAN KOTAK
        # =========================
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            f"{name} {round(confidence,1)}",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    cv2.imshow("Smart Attendance", frame)

    # ESC keluar
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()