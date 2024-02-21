#!/usr/bin/env python3
"""a module that handles session in database"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """
    A class that handles storage of session to dbase
    """

    def create_session(self, user_id=None):
        """
        a method that create session
        """
        session_id = super().create_session(userid)
        if not isinstance(session_id, str):
            return None
        kwargs = {'user_id': userid, 'session_id': session_id}
        user_session = UserSession(**kwargs)
        user_session.save()

    def user_id_for_session_id(self, session_id=None):
        """a method that overload session id"""
        try:
            user_session = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if len(user_session) < 1:
            return None
        user_session = users_session[0]
        created_at = user_session.created_at
        time = self.session_duration
        if time <= 0:
            return user_session.user_id
        if created_at + timedelta(seconds=time) >= datetime.now():
            return user_session.user_id
        return None

    def destroy_session(self, request=None):
        """a method that destroy cookie"""
        session_id = self.session_cookie(request)
        try:
            user_session = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if len(user_session) < 1:
            return False
        user_session = user_session[0]
        user_session.remove()
        return True
