#!/usr/bin/python3
""" The imported modules """
from flask import Flask, render_template
from models import storage
import os


apps = Flask(__name__)


def teardown_handle(self):
    """ The function definition """
    storage.close()


@apps.route('/hbnb_filters', strict_slashes=False)
def list_of_filters():
    """ The function definition """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template(
        "10-hbnb_filters.html",
        states=states, amenities=amenities)


if __name__ == '__main__':
    apps.run(host='0.0.0.0', port=5000)
