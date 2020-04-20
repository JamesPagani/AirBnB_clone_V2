#!/usr/bin/python3
"""Hello Flask!

A bare bones Flask web application.
Making a request to root display a string. Nothing else.
"""


from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"
