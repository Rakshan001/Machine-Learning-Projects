import cv2
import numpy as np
import dlib
from scipy.spatial import distance as dist
import face_recognition

# Eye Aspect Ratio calculation
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])  # Vertical distance
    B = dist.euclidean(eye[2], eye[4])  # Vertical distance
    C = dist.euclidean(eye[0], eye[3])  # Horizontal distance
    ear = (A + B) / (2.0 * C)
    return ear

# Thresholds and consecutive frame count for blink detection
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 3

# Counters
COUNTER = 0
TOTAL = 0

# Load the face detector and facial landmark predictor from dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Start video stream
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    rects = detector(gray, 0)
    
    for rect in rects:
        # Get the landmarks for the face
        shape = predictor(gray, rect)
        shape = np.array([[p.x, p.y] for p in shape.parts()])
        
        # Extract eye landmarks
        leftEye = shape[36:42]
        rightEye = shape[42:48]
        
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        
        ear = (leftEAR + rightEAR) / 2.0
        
        # Draw the contours around the eyes
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        
        # Blink detection
        if ear < EYE_AR_THRESH:
            COUNTER += 1
        else:
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                TOTAL += 1
            COUNTER = 0
        
        # Show blink count
        cv2.putText(frame, f"Blinks: {TOTAL}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # Here, you can decide if the person is real based on blink count
        if TOTAL >= 1:
            cv2.putText(frame, "Real Person Detected", (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Fake Detection", (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    cv2.imshow("Frame", frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
