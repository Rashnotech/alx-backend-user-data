#!/usr/bin/env python3
"""Flask module"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """return payload"""
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register():
    """a method that register users"""
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({'message': 'email already registered'}), 400
    return jsonify({'email': email, 'message': 'user created'})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """a method that handles user login"""
    email = request.form.get('email')
    pwd = request.form.get('password')
    if not (email and pwd):
        abort(401)
    session_id = AUTH.create_session(email)
    if session_id is None or not AUTH.valid_login(email, pwd):
        abort(401)
    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """a method that logout user"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """a method that display user profile"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    return jsonify({'email': user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def reset_password():
    """a method that reset password"""
    email = request.form.get('email')
    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    return jsonify({'email': email, 'reset_token': token})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
