import cv2
import numpy as np
import subprocess
import os
from picamera2 import Picamera2 

subprocess.run('export DISPLAY=:0', shell=True, executable='/bin/bash')

picam2 = Picamera2()
picam2.start()

while True:
    frame = picam2.capture_array()
    cv2.imshow("Live Video", frame)
    key = cv2.waitKey(0) & 0xFF
    
    if key == ord('q'):
        print("Exiting...")
        break

cv2.destroyAllWindows()
picam2.stop()