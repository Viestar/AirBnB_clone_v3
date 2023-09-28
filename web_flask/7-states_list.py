#!/usr/bin/python3
""" Flask running on port 5000 interactively with the storage
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page  with states sorted by name. """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session after a request."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
