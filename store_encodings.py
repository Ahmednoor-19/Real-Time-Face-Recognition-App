import face_recognition
import cv2
import os
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['face_recognition']
collection = db['known_faces']

def read_img(path):
    img = cv2.imread(path)
    (h, w) = img.shape[:2]
    width = 500
    ratio = width / float(w)
    height = int(h * ratio)
    return cv2.resize(img, (width, height))

def store_face_encodings(known_dir='known'):
    for file in os.listdir(known_dir):
        img = read_img(os.path.join(known_dir, file))
        img_enc = face_recognition.face_encodings(img)[0]
        
        # Convert encoding to list and store in MongoDB
        img_enc_list = img_enc.tolist()
        name = file.split('.')[0]
        
        document = {
            "name": name,
            "encoding": img_enc_list
        }
        
        collection.insert_one(document)

store_face_encodings()
