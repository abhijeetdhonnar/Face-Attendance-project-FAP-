# Face-Attendance-project-FAP-
The Face Attendance Project is a smart attendance system that uses facial recognition technology to automatically mark student attendance. Instead of using a manual register or RFID card, this project scans a person's face using a webcam and marks their attendance by matching the face with saved data.
# how to run the projet
step 1 
  run the EncodeGenerator.py for chaking the error 

stap 2
   run the AddDataToDatabase.py 

final step 3 
    run the main.py and open the Face-Attendance-project

# ✅ How It Works

1. Face images of students are stored in the Images/ folder.
2. EncodeGenerator.py reads all images and generates encodings.
3. Encoded data is saved in EncodeFile.p.
4. main.py opens the webcam, detects the face in real time, and matches it.
5. If the student is recognized, their attendance is marked in Firebase.

## ⚙️ Requirements

- Python 3.10 or later
- PyCharm or any Python IDE
- Webcam (for face capture)
# for the run the file without error 
## 📦 Python Libraries Used
opencv-python
- face_recognition
- cvzone
- firebase_admin
- supabase-py
- pickle
- numpy

✍️ Developed By
Abhijeet Shivaji Dhonnar
SY BCom Student, Pune University
KTHM college 
Internship Project on AI & Face Recognition
