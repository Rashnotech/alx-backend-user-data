#!/usr/bin/env python3
""" an authentication module"""
from flask import request
from typing import TypeVar, List
import re
from os import getenv


class Auth:
    """
    An authorization class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """a method that request authentication
        Return:
            path: a variable that stores the url path
            excluded_paths: a List that contains the excluded path
        """
        if path and excluded_paths and len(excluded_paths):
            for url in excluded_paths:
                url.strip()
                path += '/*'
                if re.match(url, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """a method that authorize header
        Return:
            request: a variable that takes request
        """
        if request:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """a method that keep current user
        Return
           the current requested user
        """
        return None

    def session_cookie(self, request=None):
        """a method that returns cookie value of request"""
        if request:
            session_cookie_name = getenv('SESSION_NAME', '_my_session_id')
            return request.cookies.get(session_cookie_name)
        return None
