#!/usr/bin/env python3
"""API authentication."""
from flask import request
from typing import List, TypeVar
from models.user import User


class Auth:

    """A class to manage the API authentication"""

    def __init__(self) -> None:
        """initializes the auth class"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """auth
        """
        return False

    def authentication_header(self, request=None) -> str:
        """authentication_he
        """
        return None

    def current_user(self, request=None) -> Typevar('user'):
        """current_user
        """
        return None
