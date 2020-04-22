#!/usr/bin/python3
"""Python is cool!

A bare bones Flask web application.
Making a request to /python/ will display 'Python is cool'.
You can supply some text at the end of the URL to display 'Python is <text>'.
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def what_is_python(text="is cool"):
    """Display 'Python ' and your custom text (default: is cool)."""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run()
