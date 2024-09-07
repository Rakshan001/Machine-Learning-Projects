import cv2

# Load the face cascade
face_cascade = cv2.CascadeClassifier(r'C:\Users\Asus\OneDrive\Desktop\Immortal\MACHINE LEARNING\Machine-Learning\Machine Learning Projects\haarcascacde_Face_detection\haarcascade_frontalface_default.xml')

# Read the input image
# img = cv2.imread('test.jpeg')


# Now we use video
cap=cv2.VideoCapture(0)

# cap=cv2.Videocapture('test.mp4')

while True:
    _ , img = cap.read()

# Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
    cv2.imshow('img', img)

# Wait for a key press and close the window
    # cv2.waitKey(3000)
    k=cv2.waitKey(30) &0xff
    if k==27:
        break
    
    # cv2.destroyAllWindows()

# Now release video capture object
cap.release()
