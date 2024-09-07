import face_recognition
import cv2
import numpy as np
import os
import csv
from datetime import datetime

video_capture =cv2.VideoCapture(0)


ratan_tata_image=face_recognition.load_image_file("photos/ratan-tata.png")
ratan_tata_face_encoding = face_recognition.face_encodings(ratan_tata_image)[0]


Elon_image=face_recognition.load_image_file("photos/Elon.jpg")
Elon_face_encoding = face_recognition.face_encodings(ratan_tata_image)[0]