from flask import Blueprint, request

from modules.auth.auth_controller import AuthController


bp = Blueprint("auth", __name__)


@bp.post("/login")
def login():
    payload = request.get_json()
    return AuthController.login(payload)
