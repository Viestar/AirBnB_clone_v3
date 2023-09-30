#!/usr/bin/python3
""" Flask Api Application """
import os
from models import storage
from api.v1.views import app_views
from flask import Flask, make_response
from flask import jsonify

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def shut_and_clear_everything(exception):
    """ Closes Database and clears everything """
    storage.close()


@app.errorhandler(404)
def error_404_handler(error):
    """ Handles 404 error response """
    response = make_response(jsonify({'error': "Not found"}), 404)
    return response


if __name__ == "__main__":
    port = int(os.getenv("HBNB_API_PORT", 5000))
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    app.run(host=host, port=port, threaded=True)
