#!/usr/bin/python3
""" Default RestFul API actions for users GET, PUSH, PUT, DELETE """
from models.user import User
from api.v1.views import app_views
from models import storage
from flask import abort, jsonify
from flask import make_response, request


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def do_get_all_users():
    """ Fetching users of a specific User, or user """
    users_list = []
    users = storage.all(User).values()
    for user in users:
        users_list.append(user.to_dict())
    return jsonify(users_list)


@app_views.route('/users/<user_id>/', methods=['GET'], strict_slashes=False)
def do_get_user(user_id):
    """ Retrieves a specific user based on its ID """
    user = storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def do_delete_user(user_id):
    """ Deletes a user based on the passed ID """
    user = storage.get(User, user_id)
    if user:
        storage.delete(user)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def do_post_user():
    """ Creates a user in the database """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    post_data = request.get_json()
    instance = User(**post_data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def do_update_user(user_id):
    """ Updates a user using its ID  """
    user = storage.get(user, user_id)
    if user:
        if not request.get_json():
            abort(400, description="Not a JSON")

        attributes = ['id', 'email', 'created_at', 'updated_at']

        post_data = request.get_json()
        for key, value in post_data.items():
            if key not in attributes:
                setattr(user, key, value)
        storage.save()
        return make_response(jsonify(user.to_dict()), 200)
    abort(404)
