from flask import Flask
from markupsafe import escape
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    time = datetime.datetime.now().time()
    return "Hello from flask-app 1!"

@app.route("/date")
def date():
    return "Flask-App 1: " + str(datetime.datetime.now())

if __name__ == "__main__":
    app.run()
