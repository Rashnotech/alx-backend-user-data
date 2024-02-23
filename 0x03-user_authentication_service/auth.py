#!/usr/bin/env python3
"""a module that handle authentication"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password):
    """a method that handles hashing of password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


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
        except NoResultFound:
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user
