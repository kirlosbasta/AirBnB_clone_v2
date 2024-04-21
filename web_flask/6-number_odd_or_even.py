#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''return html with Number is followed by n /number_template/<n> URL'''
    return render_template('5-number.html', n=escape(n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''return html with Number: n followed by is even | odd'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
