import face_recognition
import cv2
import os

def read_img(path):
  img = cv2.imread(path)
  (h, w) = img.shape[:2]
  width = 500
  ratio = width / float(w)
  height = int(h * ratio)
  return cv2.resize(img, (width, height))

known_encodings = []
known_names = []
known_dir = 'known'

for file in os.listdir(known_dir):
  img = read_img(os.path.join(known_dir, file))
  img_enc = face_recognition.face_encodings(img)[0]
  known_encodings.append(img_enc)
  known_names.append(file.split('.')[0])

unknown_dir = 'unknown'
for file in os.listdir(unknown_dir):
  print(file)
  img = read_img(os.path.join(unknown_dir, file))
  img_enc = face_recognition.face_encodings(img)[0]
  results = face_recognition.compare_faces(known_encodings, img_enc)
  #face_distances = face_recognition.face_distance(known_encodings, img_enc)
  #print(face_distances)

  for i in range(len(results)):
    if results[i]:
      name = known_names[i]
      (top, right, bottom, left) = face_recognition.face_locations(img)[0]
      cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
      cv2.putText(img, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
      cv2.imshow('image', img)

      cv2.waitKey(0)

  # closing all open windows
  cv2.destroyAllWindows()

  #print(results)