#!/usr/bin/env python3
"""Module of Index views"""
from flask import jsonify, abort

from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauth', methods=['GET'], strict_slashes=False)
def unauth() -> None:
    """ GET /api/v1/unauthorized
    Return:
      - 401 Unauthorized error
    """
    abort(401)
    return jsonify({"error": "unauthorized"})


@app_views.route('/Forbid', methods=['GET'], strict_slashes=False)
def Forbid() -> None:
    """ GET /api/v1/Forbidden
    Return:
      - 403 Unauthorized error
    """
    abort(403)
    return jsonify({"error": "Forbidden"})
