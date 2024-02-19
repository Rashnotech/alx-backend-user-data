#!/usr/bin/env python3
"""a view module that handles session authentication"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from api.v1.auth.basic_auth import BasicAuth
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """
    A function that handles session authentication
    """
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not email or len(email.strip()) == 0:
        return jsonify({'error': 'email missing'}), 400
    if not pwd or len(pwd.strip()) == 0:
        return jsonify({'error': 'password'}), 400
    try:
        user = User.search({'email': email})
    except Exception:
        return jsonify({'error': 'no user found for this email'}), 404
    if len(users) > 0:
        user = user[0]
    if not user.is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """a function that handles logout"""
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    return jsonify({}), 200
