#!/usr/bin/python3
""" Status Route for the Api """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def return_status():
    """ Response for a successful fetch """
    response = {"status": "OK"}
    return jsonify(response)
