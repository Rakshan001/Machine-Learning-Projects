import cv2
import os

img=cv2.imread('img/handwritten.jpeg')

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray_img,180,200,cv2.THRESH_BINARY)  #global threshold
# thresh=cv2.blur(thresh,(5,53))  #remove unwanted line smothhing the img
# ret,thresh=cv2.threshold(thresh,80,255,cv2.THRESH_BINARY)  

cv2.imshow("grayimg",gray_img)
cv2.imshow("threshold",thresh)

cv2.waitKey(0)