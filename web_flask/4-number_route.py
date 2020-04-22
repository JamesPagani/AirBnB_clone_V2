#!/usr/bin/python3
"""Is it a number?

A bare bones Flask web application.
Making a request to /number/<n> will display '<n> is a number'.
Only works if <n> is a positive integer.
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
    """Display 'C <text>', where text is your input text."""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def what_is_python(text="is cool"):
    """Display 'Python ' and your custom text (default: is cool)."""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_it_number(n):
    """Display '<n> is a number' ONLY if <n> is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run()
