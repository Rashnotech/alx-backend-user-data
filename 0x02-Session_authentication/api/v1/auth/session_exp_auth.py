#!/usr/bin/env python3
"""a module that handles expiration date in session"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """
    A class that inherits from session auth
    """

    def __init__(self) -> None:
        """Initialization"""
        super().__init__()
        session_duration_str = getenv('SESSION_DURATION')
        try:
            session_duration = int(session_duration_str)
        except (TypeError, ValueError):
            session_duration = 0

    def create_session(self, user_id=None) -> str:
        """create session"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_dict = {
                'user_id': user_id,
                'created_at': datetime.now()}
        self.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user id for session id"""
        if session_id:
            session_dict = self.user_id_by_session_id.get(session_id)
            if session_dict:
                user_id = session_dict.get('user_id')
                created_at = session_dict.get('created_at')
                if self.session_duration <= 0:
                    return user_id
                if created_at:
                    time = self.session_duration
                    if created_at + timedelta(seconds=time) >= datetime.now():
                        return user_id
        return None
