from picamera2 import Picamera2 
from libcamera import controls
import cv2
import numpy as np
import subprocess
import os
import time


subprocess.run('export DISPLAY=:0', shell=True, executable='/bin/bash')

os.environ['DISPLAY'] = ':0'

picam2 = Picamera2()
picam2.start()
print(picam2.controls)
picam2.set_controls({"AwbMode": 0})

time.sleep(2)

while True:
    frame = picam2.capture_array()
    cv2.imshow("Live Video", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Exiting...")
        break

cv2.destroyAllWindows()
picam2.stop()