#!/usr/bin/env python3
""" Auth class """
from flask import request
from typing import List, TypeVar
from .auth import Auth

class SessionAuth(Auth):
    """Session Authentication"""
    pass