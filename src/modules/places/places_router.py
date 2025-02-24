from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from common.utils import get_params
from modules.places.places_controller import PlacesController


bp = Blueprint("places", __name__, url_prefix="/places")


@bp.post("/")
def create():
    payload = request.get_json()
    return PlacesController.create(payload)


@bp.patch("/<int:id>")
@jwt_required()
def edit(id: int):
    payload = request.get_json()
    return PlacesController.edit(id, payload)


@bp.get("/")
@jwt_required()
def get_all():
    params = get_params()
    return PlacesController.get(params)


@bp.get("/<int:id>")
@jwt_required()
def get(id: int):
    return PlacesController.get_by_id(id)
