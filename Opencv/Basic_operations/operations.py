import os
import cv2
# resizing the image
img_path=os.path.join('.','img','orangecat.jpeg')
image=cv2.imread(img_path)
print(image.shape)
resized_img=cv2.resize(image,(640,480))  #Here we are using here  width and height =>output will be height and width it may be confusing take care of it
print(resized_img.shape)




cv2.imshow('catimg',image)
cv2.imshow('catimgresized',resized_img)

cv2.waitKey(0)
