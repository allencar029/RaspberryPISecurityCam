from flask_app import app
from flask import Response, render_template
import cv2
import time
from picamera2 import Picamera2 


def generate_frames():
    picam2 = Picamera2()
    picam2.stop()
    config = picam2.create_still_configuration(main={"format": "RGB888", "size": (1536, 864)})
    picam2.configure(config)
    picam2.start()

    while True:
        frame = picam2.capture_array("main")

        if frame is None:
            print("Warning: Captured empty frame.")
            time.sleep(0.1)
            continue

        x, buffer = cv2.imencode('.jpg', frame)

        if not x:
            print("Error: Could not encode frame")
            continue


        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/video')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')