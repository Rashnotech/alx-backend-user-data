#!/usr/bin/env python3
"""a module Session Auth"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """A Session Authentication Class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """a method that create session"""
        if user_id and isinstance(user_id, str):
            sess_id = uuid.uuid4()
            self.user_id_by_session_id[sess_id] = user_id
            return sess_id
        return None
