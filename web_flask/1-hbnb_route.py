#!/usr/bin/python3
"""HBNB

A bare bones Flask web application.
Making a request to '/hbnb' displays a simple string.
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays a message when making a request to root."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def simple_hbnb():
    """Display the string 'HBNB!'"""
    return "HBNB"

if __name__ == "__main__":
    app.run()
