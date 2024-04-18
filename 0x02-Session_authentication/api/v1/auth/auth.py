#!/usr/bin/env python3
""" Auth class """
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authen"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        code_path = path.rstrip('/') + '/'
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if code_path.startswith(excluded_path.rstrip('*')):
                    return False
                else:
                    pass
            elif code_path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """auth header"""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None

    def session_cookie(self, request=None):
        """session cookie"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)