import cv2 
import time
import datetime

cap = cv2.VideoCapture('/dev/video1', cv2.CAP_V4L2)

if cap.isOpened():
    print("Message: Cap is opened")
else:
    print ("Error: Could not open camera")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    x, frame = cap.read()

    if not x:
        print("Error: Failed to capture image")
        break

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 