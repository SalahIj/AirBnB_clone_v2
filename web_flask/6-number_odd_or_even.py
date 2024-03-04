#!/usr/bin/python3
""" The imported necessery modules """
from flask import Flask, render_template


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


@apps.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ The function definition
    Args:
        n: the input
    """
    return "{} is a number".format(n)


@apps.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ The function definition
    Args:
        n: the input
    """
    return render_template("5-number.html", n=n)


@apps.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ The function definition
    Args:
        n: the input
    """
    if n % 2 == 0:
        evenness = "even"
    else:
        evenness = "odd"
    return render_template("6-number_odd_or_even.html", n=n, evenness=evenness)


if __name__ == "__main__":
    apps.run(host="0.0.0.0", port="5000")
