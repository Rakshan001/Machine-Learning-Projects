import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'photos'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

# Load the images and class names
for cl in myList:
    currentImg = cv2.imread(f"{path}/{cl}")
    images.append(currentImg)
    classNames.append(os.path.splitext(cl)[0])  # Get the name without extension
print(classNames)

# Function to encode images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

# Function to mark attendance
def markAttendance(name):
    with open("Attendance.csv", "r+") as f:  # 'r+' mode to read and write
        myDataList = f.readlines()
        nameList = []
        
        # Remove any extra spaces and newlines from the names in the CSV file
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0].strip())  # Strip whitespace
        
        # Check if the student's name is already in the CSV file
        if name.strip() not in nameList:  # Strip spaces from the name
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name.strip()},{dtstring}')  # Write without extra spaces
        print(f"Current list of attendees: {nameList}")

# Find known face encodings
encodeListKnown = findEncodings(images)
print("Encodings completed")

# Capture video from webcam
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # Resize image to speed up processing
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(imgS)
    encodesCurrentFrame = face_recognition.face_encodings(imgS, facesCurrentFrame)

    # Compare faces and mark attendance
    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)  # Find the best match

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # Scale back up due to resizing
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
            markAttendance(name)  # Mark attendance for recognized face

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
