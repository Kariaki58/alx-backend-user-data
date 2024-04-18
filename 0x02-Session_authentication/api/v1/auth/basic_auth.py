#!/usr/bin/env python3
"""importing modules"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import base64
import binascii


class BasicAuth(Auth):
    """Basic Auth"""
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """extract base64 authorization header"""
        if authorization_header is None or not isinstance(
            authorization_header, str
        ):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        header_split = authorization_header.split(' ')[1]
        return header_split

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """decode base64 authorization header"""
        if type(base64_authorization_header) == str:
            try:
                get_b64 = base64.b64decode(
                    base64_authorization_header, validate=True)
                return get_b64.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """extract user credentials"""
        if decoded_base64_authorization_header is None or not isinstance(
            decoded_base64_authorization_header, str
        ):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, pwd = decoded_base64_authorization_header.split(':', 1)
        return email, pwd

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """user object from credentials"""
        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """  retrieves the User instance for a request """
        auth_header = self.authorization_header(request)
        base64_auth_header = self.extract_base64_authorization_header(
            auth_header
            )
        value = self.decode_base64_authorization_header(base64_auth_header)
        email, pwd = self.extract_user_credentials(value)
        data = self.user_object_from_credentials(email, pwd)
        return data
