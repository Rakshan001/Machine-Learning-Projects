import cv2
webcam=cv2.VideoCapture(0)
# ret=True
while True:
    ret,frame=webcam.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(40) & 0xFF ==ord('q'): #this will stop only when q button is pressed
        break
webcam.release()
cv2.destroyAllWindows()