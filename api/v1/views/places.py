#!/usr/bin/python3
""" handles all default RESTFul API actions
    for place objects
"""
from flask import Flask, request, jsonify, abort
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.state import State


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def get_city_places(city_id):
    """ Retrieves a list of all Place objects """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    places = [place.to_dict() for place in city.places]
    return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place(place_id):
    """ Retrive an place by id """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """ delete an place identified by id """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """ creates a new place in city """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    user = storage.get(User, data['user_id'])
    if user is None:
        abort(404)
    if 'name' not in data:
        abort(400, 'Missing name')
    data['city_id'] = city_id
    place = Place(**data)
    place.save()
    return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'],
                 strict_slashes=False)
def update_place(place_id):
    """ Updates place object by ID """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    keys_to_ignore = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in keys_to_ignore:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def places_search():
    """ Retrieves Place objects based on search criteria """
    data = request.get_json()

    if data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    # Extract search criteria from the JSON
    states = data.get('states', [])
    cities = data.get('cities', [])
    amenities = data.get('amenities', [])

    # If all search criteria are empty, retrieve all Place objects
    if not states and not cities and not amenities:
        places = storage.all(Place).values()
        list_places = []
        for place in places:
            list_places.append(place.to_dict())
        return jsonify(list_places)

    # Retrieve Place objects based on search criteria
    list_places = []

    # Retrieve by states and cities
    for state_id in states:
        state = storage.get(State, state_id)
        if state:
            for city in state.cities:
                if city:
                    list_places.extend(city.places)

    for city_id in cities:
        city = storage.get(City, city_id)
        if city:
            list_places.extend(city.places)

    # Filter by amenities
    if amenities:
        if not list_places:
            list_places = storage.all(Place).values()
        amenities_obj = [storage.get(Amenity, a_id) for a_id in amenities]
        list_places = [place for place in list_places
                       if all([am in place.amenities
                               for am in amenities_obj])]

    places = []
    for place in list_places:
        d = place.to_dict()
        d.pop('amenities', None)
        places.append(d)

    return jsonify(places)
