from flask import Flask
from markupsafe import escape
import datetime

app = Flask(__name__)
app.config.from_pyfile('env.py')
app.config.from_pyfile('log.py')

def getEnvString():
    return ("<b>Environment variables:</b><br>" +
            "POD_IP: " + str(app.config.get("POD_IP")) + "<br>"
            "LOG_LEVEL: " + str(app.config.get("LOG_LEVEL")) + "<br>"
            "DB_HOST: " + str(app.config.get("DB_HOST")) + "<br>"
            "DB_USER: " + str(app.config.get("DB_USER")) + "<br>"
            "DB_PASS: " + str(app.config.get("DB_PASS")) + "<br>"
            "API_KEY: " + str(app.config.get("API_KEY")) + "<br>")

@app.route("/")
def hello():
    app.logger.info('[Pod: ' + str(app.config.get("POD_IP")) + '] ' + 'Processing default request.')
    return "<h1>Hello from flask-app 1!</h1><br>" + getEnvString()

@app.route("/date")
def date():
    return "Flask-App 1: " + str(datetime.datetime.now())

if __name__ == "__main__":
    app.run()
