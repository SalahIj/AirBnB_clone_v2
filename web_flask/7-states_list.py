#!/usr/bin/python3
""" Imported necessery modules """
from flask import Flask
from models import storage
from models import *


apps = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_of_states():
    """ the function definition """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def sb_teardown(exception):
    """ the function definition
    Args:
        exception
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
