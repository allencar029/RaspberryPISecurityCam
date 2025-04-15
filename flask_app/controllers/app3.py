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

config = picam2.create_still_configuration(main={"format": "RGB888", "size": (1536, 864)})
picam2.configure(config)

picam2.start()

time.sleep(2)

# picam2.set_controls({
#     "AwbEnable": False,
#     "ColourTemperature": 3500,
#     "ColourGains": (2.5, 0.0),
# })

print("sensor format:", picam2.camera_config["main"]["format"])


while True:
    frame = picam2.capture_array("main")
    cv2.imshow("Live Video", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Exiting...")
        break

cv2.destroyAllWindows()
picam2.stop()