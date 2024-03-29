#!/usr/bin/env python3
"""a module that stores user session"""
from models.base import Base


class UserSession(Base):
    """
    A class that handles user session
    """

    def __init__(self, *arg: list, **kwargs: dict):
        """Initialization"""
        super().__init__(*args)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
