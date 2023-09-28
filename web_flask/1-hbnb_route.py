#!/usr/bin/python3
""" Flask Web framework with two routes running on localhost port 5000 """

from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
