#!/usr/bin/env python3
"""a module that implement basic auth"""
from .auth import Auth


class BasicAuth(Auth):
    """Basic authentication class"""
    def __init__(self):
        """Initialization"""
        super().__init__
