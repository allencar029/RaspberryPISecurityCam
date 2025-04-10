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

# print("here are the controls after starting the cam:", picam2.camera_controls)

time.sleep(2)

picam2.set_controls({
    "AwbEnable": False,
    "ColourTemperature": 3500,
    "ColourGains": (2.5, 0.0),
})

print("sensor format:", picam2.camera_config["main"]["format"])
# print(dir(picam2))
# print("camera controls:", picam2.controls.get_libcamera_controls())
# print("here is the controls:", picam2.camera_controls)


# time.sleep(2)

while True:
    frame = picam2.capture_array("main")
    cv2.imshow("Live Video", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Exiting...")
        break

# request = picam2.capture_request()
# frame = request.make_array("main")
# request.release()

# cv2.imwrite("/home/calle19/test_image.jpg", frame)
# cv2.imshow("Captured Frame", frame)
cv2.destroyAllWindows()
picam2.stop()