#!/usr/bin/python3
"""List of states

A web page built with Flask and with access to the MySQL database.
Requesting /states_list will display all states stored in the database.
"""


from flask import Flask, render_template
from models import storage

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display an HTML template ONLY if <n> is an integer."""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display an HTML page if <n> is an integer and if it's even or odd."""
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, n_is="even")
    else:
        return render_template("6-number_odd_or_even.html", n=n, n_is="odd")


@app.route('/states_list', strict_slashes=False)
def states_list():
    return render_template("7-states_list.html", states=storage.all())


@app.teardown_appcontext
def close_session(e):
    storage.close()


if __name__ == "__main__":
    app.run()
