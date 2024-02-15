#!/usr/bin/env python3
"""a module that implement basic auth"""
from .auth import Auth
import binascii
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """Basic authentication class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract basic authentication"""
        if authorization_header is None or not \
           isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split('Basic')[1].strip()

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """decoding base 64 authorization header"""
        if base64_authorization_header is None or not \
           isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """extract user credential"""
        if decoded_base64_authorization_header is None \
           or not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        try:
            user, password = decoded_base64_authorization_header.split(':')
            return (user, password)
        except Exception:
            return (None, None)

    def user_object_from_credentials(self, user_email:
                                     str, user_pwd: str) -> TypeVar('User'):
        """User object"""
        from models.user import User

        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        user_info = {'email': user_email}
        try:
            users = User.search(user_info)
        except Exception:
            return None
        if len(users) > 0:
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves the current user"""
        auth_header = self.authorization_header(request)
        auth_code = self.extract_base64_authorization_header(auth_header)
        auth_decoded = self.decode_base64_authorization_header(auth_code)
        email, pwd = self.extract_user_credentials(auth_decoded)
        user = self.user_object_from_credentials(email, pwd)
        return user
