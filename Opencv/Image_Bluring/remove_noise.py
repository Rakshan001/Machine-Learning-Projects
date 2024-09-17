import cv2
import os

img_path=os.path.join('.','img','noise_img.jpeg')
img=cv2.imread(img_path)
cv2.imshow("noisy_img",img)
'''classical Blur'''
k_size=3  #it the number of neighbors we are considering take average for blurring
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