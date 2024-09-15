# Real-Time Face Recognition App

This project implements a real-time face recognition system using a webcam. The application captures images from the webcam, detects faces, and recognizes known individuals using a face recognition library. Face encodings and metadata are stored in a MongoDB database, and a Streamlit interface is used to interact with the application.

## Project Structure

### Files in the Repository

1. **`streamlit_app.py`**
   - The main Streamlit application file that provides the user interface for face recognition. It includes features for capturing images, recognizing faces, and adding new faces to the database.

2. **`functions.py`**
   - Contains the core functions for face recognition, including capturing images, encoding faces, and interacting with MongoDB.

3. **`requirements.txt`**
   - Lists the Python libraries required to run the application.

### Required Libraries

- **Streamlit**: Provides the web interface for interacting with the face recognition system.
- **face_recognition**: Library for face detection and recognition.
- **opencv-python**: For capturing images from the webcam.
- **pymongo**: For interacting with MongoDB.
- **Pillow**: For image processing tasks.

## Features

1. **Real-Time Face Detection**: Capture images from the webcam and detect faces in real time.
2. **Face Recognition**: Recognize known individuals based on face encodings stored in the MongoDB database.
3. **Add New Faces**: Add new face encodings to the database through the Streamlit interface.
4. **Face Encoding Storage**: Store face encodings and metadata in MongoDB for future recognition.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/real-time-face-recognition-app.git
cd real-time-face-recognition-app
```

### 2. Install Dependencies
Install the required Python packages using requirements.txt.

```bash
pip install -r requirements.txt
```

### 3. Set Up MongoDB
Ensure MongoDB is running and create a database to store face encodings and metadata.

### 4. Run the Streamlit App
Start the Streamlit application using the following command:

```bash
streamlit run streamlit_app.py
```

The application will open in your default web browser, and you can interact with it to capture images, recognize faces, and manage face encodings.

## Usage

1. **Capture Image**: 
   - Click the button to open the webcam.
   - Capture an image of a face using the webcam interface.

2. **Add New Face**: 
   - Enter a name for the individual.
   - Click the button to add the captured face encoding to the MongoDB database.

3. **Recognize Face**: 
   - The application will automatically detect and recognize faces in real-time.
   - It will display the name of the recognized individual if their face is found in the database.

## Future Enhancements

- **Enhanced Recognition Accuracy**: 
  - Improve the accuracy of face recognition by incorporating advanced algorithms or training on additional datasets.

- **User Management**: 
  - Implement features for managing users, including updating and deleting face encodings.

- **Cross-Platform Support**: 
  - Enhance compatibility to support different operating systems and hardware configurations.

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for more information.

Contact
For any questions or suggestions, please feel free to reach out to:

Sheikh Ahmed Noor
Email: sheikhahmednoor00@gmail.com
