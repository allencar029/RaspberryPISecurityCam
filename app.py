import cv2
import numpy as np
import subprocess

subprocess.run(["libcamera-still", "-o", "image.jpg", "--width", "640", "--height", "480"])

frame = cv2.imread("image.jpg")

if frame is None:
    print("Error: Failed to load image")
else:
    cv2.imshow("Camera", frame)
    cv2.waitKey(0)

cv2.destroyAllWindows()
