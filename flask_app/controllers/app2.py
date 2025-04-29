from flask_app import app
from flask import Response, render_template
import cv2
import time
from picamera2 import Picamera2
from libcamera import controls 

WIDTH = 1280 
HEIGHT = 720
FRAMERATE = 25
JPEG_QUALITY = 60

def generate_frames():
    picam2 = None
    try:
        picam2 = Picamera2()
        picam2.stop()
        config = picam2.create_video_configuration(
            main={
                "format": "YUV420", 
                "size": (WIDTH, HEIGHT)
            },
            controls={
                "FrameRate": FRAMERATE,
            }
        )
        picam2.configure(config)
        picam2.start()

        while True:
            frame_yuv = picam2.capture_array("main")

            if frame_yuv is None:
                print("Warning: Captured empty frame.")
                time.sleep(0.1)
                continue

            frame_rgb = cv2.cvtColor(frame_yuv, cv2.COLOR_YUV2RGB_I420)

            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY]
            x, buffer = cv2.imencode('.jpg', frame_rgb, encode_param)

            if not x:
                print("Error: Could not encode frame")
                continue


            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
            
    finally:
        if picam2 and picam2.started:
            picam2.stop()


@app.route('/video')
def video_feed():
    headers = {
        'Cache-Control': 'no-store, no-cache, must-revalidate, pre-check=0, post-check=0, max-age=0',
        'Pragma': 'no-cache',
        'Expires': '-1'
    }
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame', headers=headers)

@app.route('/')
def index():
    return render_template('index.html')