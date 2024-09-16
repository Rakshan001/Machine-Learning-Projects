import cv2

img=cv2.imread('img/orangecat.jpeg')
print(img.shape)

croped_img=img[30:315, 40:400]
print(croped_img.shape)
cv2.imshow("img",img)
cv2.imshow("cropedimg",croped_img)

cv2.waitKey(0)