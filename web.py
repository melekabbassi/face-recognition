from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/face_recognition")
def face_recognition():
    return ("<p>Face Recognition</p>"
            "<p>Face Recognition</p>")