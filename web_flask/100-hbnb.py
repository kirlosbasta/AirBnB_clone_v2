#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    '''return html page about hbnb_filter'''
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exec):
    '''Remove the current session after each request'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
