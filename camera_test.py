import cv2

cap = cv2.VideoCapture(1)

# Kurangi buffer biar tidak freeze
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Gagal membaca frame")
        break

    cv2.imshow("HP Camera", frame)

    # Delay kecil agar frame update
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()