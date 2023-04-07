from flask import Flask, redirect, render_template, Response, url_for
from weapon_detection import VideoCamer
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alert')
def alert():
    return render_template('alert.html')



def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        
@app.route('/video_feed')

def video_feed():
    return Response(gen(VideoCamer()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/success')
def success():
    return render_template('sat.html')


if __name__ == '__main__':    
    app.run(host='0.0.0.0',port=5100, debug=True)
