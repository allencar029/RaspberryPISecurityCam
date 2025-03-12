import cv2 
import time
import datetime

cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L2)

if cap.isOpened():
    print("Message: Cap is opened")
else:
    print ("Error: Could not open camera")
    exit()

print("Width:", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    x, frame = cap.read()
    print(x)
    print(frame)

    if not x or frame is None:
        print("Error: Failed to capture image")
        break

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 