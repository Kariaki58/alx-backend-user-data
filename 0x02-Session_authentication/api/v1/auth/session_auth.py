#!/usr/bin/env python3
""" Auth class """
from flask import request
from typing import List, TypeVar
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Session Authentication"""
    user_id_by_session_id = {}
    
    def create_session(self, user_id: str = None) -> str:
        """create session function"""
        if user_id is None:
            return None
        if  isinstance(user_id, str):
            return None
        else:
            session_id = uuid4()
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id
    
            
