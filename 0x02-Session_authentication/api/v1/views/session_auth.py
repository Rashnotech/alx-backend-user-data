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
    password = request.form.get('password')

    if not email:
        return jsonify({'error': 'email missing'}), 400
    if not password:
        return jsonify({'error': 'password'})
    user = User.search({'email': email})
    if not user:
        return jsonify({'error': 'no user found for this email'}), 404
    if user[0].is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401
    from api.v1.app import auth
    user = user[0]
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    return response
