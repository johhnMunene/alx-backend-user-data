#!/usr/bin/env python3
"""API authentication module.

This module contains the Auth class which is responsible for handling
API authentication, including checking if a request requires
authentication, extracting the authentication header, and determining
the current user based on the request.
"""

from flask import request
from typing import List, TypeVar
from models.user import User


class Auth:
    """A class to manage API authentication.

    This class provides methods to determine if a request requires
    authentication, to extract the authentication header from the request,
    and to get the current user associated with the request.
    """

    def __init__(self) -> None:
        """Initializes the Auth class."""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if the given path requires authentication.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not require authentication.

        Returns:
            bool: True if the path requires authentication, False otherwise.
        """
        if path is None:
            return True
        if not excluded_paths or len(excluded_paths) == 0:
            return True

        # Normalize path to ensure trailing slashes are treated equivalently
        normalized_path = path.rstrip('/') + '/'

        for ex_path in excluded_paths:
            if ex_path == normalized_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header from the request.

        Args:
            request: The Flask request object (optional).

        Returns:
            str: None always, as this method will be implemented later.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user based on the request.

        Args:
            request: The Flask request object (optional).

        Returns:
            TypeVar('User'): None always, as this method will be implemented later.
        """
        return None
