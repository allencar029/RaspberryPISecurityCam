from flask_app import app
from flask import Response, render_template
import cv2
import numpy as np
import subprocess
import os
import time
from picamera2 import Picamera2 

subprocess.run('export DISPLAY=:0', shell=True, executable='/bin/bash')

os.environ['DISPLAY'] = ':0'

picam2 = Picamera2()

picam2.stop()

config = picam2.create_still_configuration(main={"format": "RGB888", "size": (1536, 864)})
picam2.configure(config)

picam2.start()

def generate_frames():
    while True:
        frame = picam2.capture_array("main")
        x, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/video')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')