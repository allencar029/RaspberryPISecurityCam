from flask_app import app
from flask import Response, render_template
import cv2
import numpy as np
import subprocess
import os
from picamera2 import Picamera2 
from libcamera import controls

subprocess.run('export DISPLAY=:0', shell=True, executable='/bin/bash')

os.environ['DISPLAY'] = ':0'

picam2 = Picamera2()
picam2.start()
picam2.set_controls({"AwbMode": "auto"})

while True:
    frame = picam2.capture_array()
    cv2.imshow("Live Video", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Exiting...")
        break

cv2.destroyAllWindows()
picam2.stop()

def generate_frames():
    while True:
        frame = picam2.capture_array()
        x, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--framern'
               b'Content-Type: image/jpegrnrn' + frame_bytes + b'rn')
        

app.route('/video')
def root():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

app.route('/')
def index():
    return render_template('index.html')