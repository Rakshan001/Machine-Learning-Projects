import cv2
import numpy as np
import face_recognition
import os

path = 'photos'
images = []
classNames=[]
myList = os.listdir(path)
print(myList)

for cl in myList:
    currentImg=cv2.imread(f"{path}/{cl}") #we can use load_img but we have open cv imread method
    images.append(currentImg)
    classNames.append(os.path.splitext(cl)[0]) # we need only name of the img file not include the .png or .jpg
print(classNames)


# Now we need to find the encoding of the each images 

def findEncodings(images):
    encodeList = []
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode =face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

encodeListKnown =findEncodings(images)
print("Encoding comepleted")

# Find matches between encodings


# we capture photo from
cap=cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.5,0.5) # we need to resize the images so that it speed up the proccess
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    facesCurrentFrame=face_recognition.face_locations(imgS)
    encodesCurrentFrame,facesCurrentFrame = face_recognition.face_encodings(imgS,facesCurrentFrame)


