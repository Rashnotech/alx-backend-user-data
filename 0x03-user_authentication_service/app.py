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
    """a module that register users"""
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        if not (email and password):
            abort(400)
        AUTH.register_user(email, password)
    except Exception:
        return jsonify({'message': 'email already registered'})
    return jsonify({'email': email, 'message': 'user created'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
