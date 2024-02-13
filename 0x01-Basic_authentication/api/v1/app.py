#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = getenv('AUTH_TYPE', None)
app.register_blueprint(app_views)


if auth:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def handle_request():
    """a middleware method"""
    if auth:
        exempt_endpoints = [
            '/api/v1/status/',
            '/api/v1/unauthorized/',
            '/api/v1/forbidden/'
            ]
        if auth.require_auth(request.path, exempt_endpoints):
            if not auth.authorization_header(request):
                abort(401)
            if not auth.current_user(request):
                abort(403)


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Handling unauthorized"""
    return jsonify({'error': 'Unauthorized'}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Handle forbidden"""
    return jsonify({'error': 'Forbidden'}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
