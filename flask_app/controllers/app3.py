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
picam2.stop()
picam2.start()

time.sleep(2)

print(dir(picam2))
print("camera controls:", picam2.controls.get_libcamera_controls())
print("here is the controls:", picam2.camera_controls)

while True:

    picam2.set_controls({
        "AwbEnable": False,
        "AeEnable": False,
        "ColourTemperature": 4500,
        "ColourGains": (1.5, 2.0),
    })
    print("controls after:", picam2.controls)

    time.sleep(2)
    frame = picam2.capture_array("main")
    # frame.set_controls({
    #     "AwbEnable": False,
    #     "AeEnable": False,
    #     "ColourTemperature": 4500,
    #     "ColourGains": (1.5, 2.0),
    # })
    cv2.imshow("Live Video", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Exiting...")
        break

cv2.destroyAllWindows()
picam2.stop()