#!/usr/bin/python3
""" The imported modules """
from flask import Flask, render_template
from models import *
from models import storage


apps = Flask(__name__)


@apps.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ The function definition
    Args:
        state_id:
    """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@apps.teardown_appcontext
def db_teardown(exception):
    """The function definition
    Args:
        execption:
    """
    storage.close()


if __name__ == '__main__':
    apps.run(host='0.0.0.0', port='5000')
