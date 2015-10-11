import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! It's FLASK! And hopefully, WORKING again!"