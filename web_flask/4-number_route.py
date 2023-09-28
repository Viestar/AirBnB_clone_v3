#!/usr/bin/python3
""" Flask Web framework with two routes running on localhost port 5000 """

from flask import Flask, render_template

# Creating a Flask instance.
app = Flask(__name__)


# Routes
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns default html with a passed string """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns default html with a passed string """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hbnb_variable(text):
    """ Returns default html with a passed string """
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_variable(text='is cool'):
    """ Returns default html with a passed string """
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """display n if integer"""
    return "%i is a number" % n


if __name__ == "__main__":
    # Clarifying listening port and IP
    app.run(host="0.0.0.0", port=5000)
