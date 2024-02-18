#!/usr/bin/env python3
"""a module Session Auth"""
from .auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """A Session Authentication Class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """a method that create session"""
        if user_id and isinstance(user_id, str):
            sess_id = str(uuid.uuid4())
            self.user_id_by_session_id[sess_id] = user_id
            return sess_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """a method that get user id"""
        if session_id and isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        """a method that return user instance based on cookie value"""
        session_id = self.session_cookie(request)
        if session_id:
            user_id = self.user_id_for_session_id(session_id)
            if user_id:
                return User.get(user_id)
        return None

    def destroy_session(self, request=None):
        """a method that deletes the user session/ logout"""
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                if self.user_id_for_session_id(session_id):
                    del self.user_id_by_session_id[session_id]
                    return True
        return False
