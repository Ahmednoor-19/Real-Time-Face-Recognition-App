import streamlit as st
import cv2
from functions import load_known_faces, recognize_face, save_face
import face_recognition
import numpy as np

# Load known faces and encodings
known_encodings, known_names = load_known_faces()

st.title("Face Recognition App")

# Sidebar to select different pages
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page", ["Recognize Face", "Add New Face"])

# Initialize camera
cap = None

if page == "Recognize Face":
    # Button to start webcam feed
    if st.button("Open Webcam", key="open_webcam_button"):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            cap = cv2.VideoCapture(1)
        if not cap.isOpened():
            st.write("No camera found. Please connect a webcam.")
            cap = None

        if cap is not None:
            stframe = st.empty()  # Placeholder for displaying the feed

            # Capture and process frames
            while True:
                ret, frame = cap.read()
                if ret:
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    stframe.image(frame_rgb, channels="RGB")
                    
                    # Recognize faces in the image
                    names = recognize_face(frame, known_encodings, known_names)
                    
                    # Display recognized names
                    if names:
                        st.write(f"Recognized: {', '.join(names)}")
                    else:
                        st.write("No known faces detected.")
                else:
                    st.write("Failed to capture image. Please try again.")
                    
                # Break the loop if the user closes the app
                if not st.session_state.get('webcam_open', False):
                    break

            # Release the webcam
            cap.release()

elif page == "Add New Face":
    st.header("Add a New Face")

    # Input name
    new_name = st.text_input("Enter the name of the person")

    # File uploader for image input
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None and new_name:
        # Convert the file to an OpenCV image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the uploaded image
        st.image(frame_rgb, channels="RGB", caption="Uploaded Image", use_column_width=True)

        # Save the face encoding and image with the new name
        face_encodings = face_recognition.face_encodings(frame_rgb)
        if face_encodings:
            save_face(new_name, face_encodings[0])
            st.write(f"Face saved for {new_name}")
        else:
            st.write("No face detected. Please try again.")