#!/usr/bin/env python3
"""a module that handle authentication"""
import bcrypt


def _hash_password(password):
    """a method that handles hashing of password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
