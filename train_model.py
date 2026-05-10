import cv2
import os
import numpy as np
from PIL import Image

dataset_path = "dataset"

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
ids = []

label_ids = {}
current_id = 0

for file in os.listdir(dataset_path):

    path = os.path.join(dataset_path, file)

    image = Image.open(path).convert('L')

    image_np = np.array(image, 'uint8')

    name = file.split("_")[0]

    if name not in label_ids:
        label_ids[name] = current_id
        current_id += 1

    id = label_ids[name]

    faces.append(image_np)
    ids.append(id)

recognizer.train(faces, np.array(ids))

recognizer.save("trainer/trainer.yml")

print("Training selesai!")

print(label_ids)