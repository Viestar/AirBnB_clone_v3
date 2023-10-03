#!/usr/bin/python3
""" Default RestFul API actions for reviews GET, PUSH, PUT, DELETE """
from models.review import Review
from models.place import Place
from models.user import User
from api.v1.views import app_views
from models import storage
from flask import abort, jsonify
from flask import make_response, request


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(place_id):
    """ Fetching reviews of a specific place """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)
    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """ Fetches a Review object """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """ Deletes a review based on the passed ID """
    review = storage.get(Review, review_id)

    if not review:
        abort(404)
    storage.delete(review)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def post_review(place_id):
    """ Creates a Review """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")
    f_data = request.get_json()
    user = storage.get(User, f_data['user_id'])

    if not user:
        abort(404)
    if 'text' not in request.get_json():
        abort(400, description="Missing text")
    f_data['place_id'] = place_id
    instance = Review(**f_data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def put_review(review_id):
    """ Creates a review in the database """
    review = storage.get(Review, review_id)

    if not review:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
    f_data = request.get_json()
    for key, value in f_data.items():
        if key not in ignore:
            setattr(review, key, value)
    storage.save()
    return make_response(jsonify(review.to_dict()), 200)
