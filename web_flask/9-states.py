#!/usr/bin/python3
""" The imported modules """
from flask import Flask, render_template
from models import *
from models import storage


apps = Flask(__name__)


@apps.route('/states', strict_slashes=False)
@apps.route('/states/<state_id>', strict_slashes=False)
def list_of_states(state_id=None):
    """ The function definition """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@apps.teardown_appcontext
def db_teardown(exception):
    """The function definition
    Args:
        execption:
    """
    storage.close()


if __name__ == "__main__":
    apps.run(host='0.0.0.0', port='5000')
