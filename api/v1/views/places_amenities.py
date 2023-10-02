#!/usr/bin/python3
""" Default RestFul API actions handler for Place - Amenity"""
from os import environ
from flask import abort, jsonify
from flask import make_response, request
from models.place import Place
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views


@app_views.route('places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def do_get_all_place_amenities(place_id):
    """ Fetching a list of the amenity objects of a Place """
    place = storage.get(Place, place_id)

    if place:
        if environ.get('HBNB_TYPE_STORAGE') == "db":
            amenities = [amenity.to_dict() for amenity in place.amenities]
        else:
            amenities = [storage.get(Amenity, amenity_id).to_dict()
                         for amenity_id in place.amenity_ids]
        return jsonify(amenities)
    abort(404)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def do_delete_an_amenity(place_id, amenity_id):
    """ Deletes an Amenity object of a Place  """
    place = storage.get(Place, place_id)

    if place:

        amenity = storage.get(Amenity, amenity_id)

        if amenity:

            if environ.get('HBNB_TYPE_STORAGE') == "db":
                if amenity in place.amenities:
                    place.amenities.remove(amenity)
                abort(404)
            else:
                if amenity_id in place.amenity_ids:
                    place.amenity_ids.remove(amenity_id)
                abort(404)
            storage.save()
            return jsonify({}), 200
        abort(404)
    abort(404)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['POST'], strict_slashes=False)
def post_place_amenity(place_id, amenity_id):
    """ Links an Amenity object to a Place  """
    place = storage.get(Place, place_id)

    if place:
        amenity = storage.get(Amenity, amenity_id)
        if amenity:
            if environ.get('HBNB_TYPE_STORAGE') == "db":
                if amenity in place.amenities:
                    return jsonify(amenity.to_dict()), 200
                else:
                    place.amenities.append(amenity)
            else:
                if amenity_id in place.amenity_ids:
                    return jsonify(amenity.to_dict()), 200
                else:
                    place.amenity_ids.append(amenity_id)
            storage.save()
            return jsonify(amenity.to_dict()), 201
        abort(404)
    abort(404)
