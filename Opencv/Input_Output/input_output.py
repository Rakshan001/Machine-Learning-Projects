import os

import cv2

#read image
image_path=os.path.join('.','img','orangecat.jpeg')

img=cv2.imread(image_path)
print(img.shape)

#write image

# ('current directory',"folder name",'img-name-for saving the img'),refering img which need to be saved
cv2.imwrite(os.path.join('.','img','orangecat_out.jpeg'),img)

# visulaize image
cv2.imshow('imga',img)
# cv2.waitKey(0)

''' Video processing'''
# video read

video = cv2.VideoCapture('img/Diana_Cropped_17.mp4')

# visualize the video
ret=True
while True:
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame',frame)
        cv2.waitKey(10)
    video.release()  #this is important to free the memmory
    cv2.destroyAllWindows
