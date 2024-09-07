import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file("photos/Elon.jpg")
# convert img into RGB
imgElon=cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file("photos/ElonTest.jpg")
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)




# Detecting the face
faceLoc=face_recognition.face_locations(imgElon)[0]
# encoding the face detected
encodeElon=face_recognition.face_encodings(imgElon)
cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255))


# print(faceLoc)


cv2.imshow('Elon Musk',imgElon)
cv2.imshow('Elon Test',imgTest)

cv2.waitKey(0)