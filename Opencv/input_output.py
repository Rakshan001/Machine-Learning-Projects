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

