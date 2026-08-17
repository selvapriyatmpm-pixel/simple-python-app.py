from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Selva! Welcome to my Python Web Application."
