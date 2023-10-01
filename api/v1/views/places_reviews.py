#!/usr/bin/python3
""" Default RestFul API actions for reviews GET, PUSH, PUT, DELETE """
from models.review import Review
from models.place import Place
from models.user import User
from api.v1.views import app_views
from models import storage
from flask import abort, jsonify
from flask import make_response, request


@app_views.route('/places/<places_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def do_get_all_reviews(places_id):
    """ Fetching reviews of a specific place """
    reviews_list = []
    place = storage.get(Place, places_id)
    if place:
        for review in place.reviews:
            reviews_list.append(review.to_dict())
        return jsonify(reviews_list)
    abort(404)


@app_views.route('/reviews/<review_id>/', methods=['GET'],
                 strict_slashes=False)
def do_get_review(review_id):
    """ Retrieves a specific review based on its ID """
    review = storage.get(Review, review_id)
    if review:
        return jsonify(review.to_dict())
    abort(404)


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def do_delete_review(review_id):
    """ Deletes a review based on the passed ID """
    review = storage.get(Review, review_id)
    if review:
        storage.delete(review)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)


@app_views.route('/places/<places_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def do_post_review(place_id):
    """ Creates a review in the database """
    place = storage.get(Place, place_id)
    if place:
        if not request.get_json():
            abort(400, description="Not a JSON")
        if 'user_id' not in request.get_json():
            abort(400, description="Missing user_id")

        post_data = request.get_json()
        user = storage.get(User, post_data['user_id'])
        if user:
            if 'text' in request.get_json():
                post_data['place_id'] = place_id
                instance = Review(**post_data)
                instance.save()
                return make_response(jsonify(instance.to_dict()), 201)
            abort(400, description="Missing text")
        abort(404)
    abort(404)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def do_update_review(review_id):
    """ Updates a review using its ID  """
    review = storage.get(Review, review_id)
    if review:
        if not request.get_json():
            abort(400, description="Not a JSON")

        atts = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']

        post_data = request.get_json()
        for key, value in post_data.items():
            if key not in atts:
                setattr(review, key, value)
        storage.save()
        return make_response(jsonify(review.to_dict()), 200)
    abort(404)
