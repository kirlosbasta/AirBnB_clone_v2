#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exec):
    '''Remove the current session after each request'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
