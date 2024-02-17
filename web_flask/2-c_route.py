#!/usr/bin/python3
""" Imported the necessery modules"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HB():
    """ The function definition """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HB():
    """ The function definition """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """ The function definition
    Args:
        text: the input
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
