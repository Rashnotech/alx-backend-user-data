#!/usr/bin/env python3
"""a module that handle authentication"""
import bcrypt
from db import DB
import uuid
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import User


def _hash_password(password):
    """a method that handles hashing of password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """a method that generate uuid"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """a method that register users"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"<user's {email}> already exists")
        except (InvalidRequestError, NoResultFound):
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """a method that validate credentials"""
        try:
            user = self._db.find_user_by(email=email)
            pwd = user.hashed_password
            return bcrypt.checkpw(password.encode('utf-8'), pwd)
        except (InvalidRequestError, NoResultFound):
            return False
        return False

    def create_session(self, email: str):
        """a method that creates a session"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
        except (InvalidRequestError, NoResultFound):
            return None
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """a method that get the user session id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except (InvalidRequestError, NoResultFound):
            return None
