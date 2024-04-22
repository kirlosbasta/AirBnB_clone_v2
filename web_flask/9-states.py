#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    '''return html page of with all the states from /states URL'''
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    '''return html page with cities from state with id id '''
    states = storage.all("State")
    state = None
    for key in states:
        if id in key:
            state = states[key]
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(exec):
    '''Remove the current session after each request'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
