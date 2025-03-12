import cv2
import numpy as np
import subprocess
import os

os.environ['Display'] = ':0'

subprocess.run(["libcamera-still", "-o", "image.jpg", "--width", "640", "--height", "480"])

frame = cv2.imread("image.jpg")

if frame is None:
    print("Error: Failed to load image")
else:
    cv2.imshow("Camera", frame)
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Exiting...")
            break

cv2.destroyAllWindows()
