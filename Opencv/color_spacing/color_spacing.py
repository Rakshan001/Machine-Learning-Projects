import cv2
import os

img=cv2.imread('img/orangecat.jpeg')

rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# cv2.imshow('image',img)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('image',img)
cv2.imshow('rgb_image',rgb_img)
cv2.imshow('gray_image',gray_img)
cv2.imshow('hsv_image',hsv_img)




cv2.waitKey(0)