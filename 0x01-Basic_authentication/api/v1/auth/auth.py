#!/usr/bin/env python3
""" an authentication module"""
from flask import request
from typing import TypeVar, List


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
        return False


    def authorization_header(self, request=None) -> str:
        """a method that authorize header
        Return:
            request: a variable that takes request
        """
        return request


    def current_user(self, request=None) -> TypeVar('User'):
        """a method that keep current user
        Return
           the current requested user
        """
        return request
