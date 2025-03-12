import cv2 
import time
import datetime

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

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