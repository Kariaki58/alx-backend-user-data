#!/usr/bin/env python3
""" Auth class """
from flask import request
from typing import List, TypeVar
from ..views.users import User
from .auth import Auth
from uuid import uuid4, UUID
import os


class SessionAuth(Auth):
    """Session Authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create session function"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        else:
            session_id = uuid4()
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user id for session id"""
        if session_id is None or isinstance(session_id, str):
            return None
        else:
            user_id = SessionAuth.user_id_by_session_id.get(session_id)
            return user_id

    def current_user(self, request=None):
        """return if a user session exists"""
        if not request:
            return None
        session_id = self.session_cookie(request)
        if not session_id:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return None

        return User.get(user_id)
