import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file("photos/Elon.jpg")

# convert img into RGB
imgElon=cv2.cvtColor(imgElon,cv2.COLOR_BGR2)