#!/usr/bin/python3
"""C is fun!

A bare bones Flask web application.
Making a request to '/c/<text>' will print a string along with <text>.
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a message when making a request to root."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def simple_hbnb():
    """Display the string 'HBNB!'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def what_is_c(text):
    """Display 'C is <text>', where text is your input text."""
    return "C is {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run()
