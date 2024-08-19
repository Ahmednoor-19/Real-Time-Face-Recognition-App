import face_recognition
import cv2
import numpy as np
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['face_recognition']
collection = db['known_faces']


#def read_img(path):
#    img = cv2.imread(path)
#    (h, w) = img.shape[:2]
#    width = 500
#    ratio = width / float(w)
#    height = int(h * ratio)
#    return cv2.resize(img, (width, height))

def load_known_faces():
    known_encodings = []
    known_names = []

    documents = collection.find()
    for doc in documents:
        name = doc['name']
        encoding = np.array(doc['encoding'])
        known_encodings.append(encoding)
        known_names.append(name)

    return known_encodings, known_names

def recognize_face(frame, known_encodings, known_names):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]
        
        names.append(name)
    
    return names

def save_face(name, face_encoding):
    # Convert encoding to list and store in MongoDB
    img_enc_list = face_encoding.tolist()
    
    document = {
        "name": name,
        "encoding": img_enc_list
    }
    
    collection.insert_one(document)