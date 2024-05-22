#!/usr/bin/env python3
"""API authentication."""
from flask import request


class Auth:
    def require_auth(self, excluded_path=List[str]) -> bool:
        """auth
        """
        return False

    def authentication_header(self, request=None) -> str:
        """
        """
        return None

    def current_user(self, request=None) -> Typevar('user'):
        """
        """
        return None
