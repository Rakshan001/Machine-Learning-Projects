import cv2
import os
''' Image Blurring'''
img_path=os.path.join(".","img","parrot.jpeg")
img=cv2.imread(img_path)

'''classical Blur'''
k_size=11  #it the number of neighbors we are considering take average for blurring
img_blur=cv2.blur(img,(k_size,k_size))


'''Gaussian Blur'''
img_guassianblur=cv2.GaussianBlur(img,(k_size,k_size),90)

'''Median Blur'''
img_medianBlur=cv2.medianBlur(img,k_size)


cv2.imshow('parrot',img)
cv2.imshow('parrot_blur',img_blur)
cv2.imshow('parrot_gaussianblur',img_guassianblur)
cv2.imshow('parrot-medianblur',img_medianBlur)
cv2.waitKey(0)