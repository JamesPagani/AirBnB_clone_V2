#!/usr/bin/python3
"""Hello Flask!

A bare bones Flask web application.
Making a request to root display a string. Nothing else.
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays a message when making a request to root."""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
