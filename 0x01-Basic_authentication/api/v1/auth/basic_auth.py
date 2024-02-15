#!/usr/bin/env python3
"""a module that implement basic auth"""
from .auth import Auth
import binascii
import base64


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
