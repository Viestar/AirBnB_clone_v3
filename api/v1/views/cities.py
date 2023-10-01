#!/usr/bin/python3
""" Default RestFul API actions for cities GET, PUSH, PUT, DELETE """
from flask import abort, jsonify
from flask import make_response, request
from models.city import City
from models.state import State
from api.v1.views import app_views
from models import storage


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def do_get_all_cities(state_id):
    """ Fetching cities of a specific State, or city """
    cities_list = []
    state = storage.get(State, state_id)
    if state:
        for city in state.cities:
            cities_list.append(city.to_dict())
        return jsonify(cities_list)
    abort(404)


@app_views.route('/cities/<city_id>/', methods=['GET'], strict_slashes=False)
def do_get_city(city_id):
    """ Retrieves a specific city based on its ID """
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def do_delete_city(city_id):
    """ Deletes a city based on the passed ID """
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def do_post_city(state_id):
    """ Creates a City in the database """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    post_data = request.get_json()
    instance = City(**post_data)
    instance.state_id = state.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def do_update_city(city_id):
    """ Updates a City using its ID  """
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'state_id', 'created_at', 'updated_at']

    post_data = request.get_json()
    for key, value in post_data.items():
        if key not in ignore:
            setattr(city, key, value)
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)
