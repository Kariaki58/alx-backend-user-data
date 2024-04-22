#!/usr/bin/env python3
import bcrypt


def _hash_password(password):
    salt = bcrypt.gensalt()
    password_en = password.encode("utf-8")
    return bcrypt.hashpw(password_en, salt)