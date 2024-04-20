#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''return Hello HBNB! for root URL'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''return HBNB for /hbnb URL'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    '''return C followed by text for /c/<text> URL'''
    return f"C {escape(text).replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_route(text='is cool'):
    '''return Python followed by text for /python/<text> URL'''
    return f"Python {escape(text).replace('_', ' ')}"


@app.route('/number/<int:n>')
def number(n):
    '''return n is a number for /number/<n> URL'''
    return f"{escape(n)} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
