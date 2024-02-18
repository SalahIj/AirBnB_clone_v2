#!/usr/bin/python3
""" The imported necessery modules """
from flask import Flask


apps = Flask(__name__)


@apps.route("/", strict_slashes=False)
def hello():
    """ The function description """
    return "Hello HBNB!"


@apps.route("/hbnb", strict_slashes=False)
def hbnb():
    """ The function description """
    return "HBNB"


@apps.route("/c/<text>", strict_slashes=False)
def text(text):
    """ The function definition
    Args:
        text: the input
    """
    return "C {}".format(text.replace("_", " "))


@apps.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@apps.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """ The function definition
    Args:
        text: the input
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    apps.run(host="0.0.0.0", port="5000")
