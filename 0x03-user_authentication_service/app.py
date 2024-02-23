#!/usr/bin/env python3
"""Flask module"""
from flask import Flask, jsonify, request
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
    try:
        email = request.form.get('email')
        pwd = request.form.get('password')
        if AUTH.valid_login(email, password):
            return jsonify({'email': email, 'message': 'logged in'})
    except ValueError:
        abort(401)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
