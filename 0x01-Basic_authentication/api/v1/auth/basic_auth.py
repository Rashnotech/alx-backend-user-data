#!/usr/bin/env python3
"""a module that implement basic auth"""
from .auth import Auth


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
