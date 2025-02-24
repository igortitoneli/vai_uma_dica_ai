from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from common.utils import get_jwt_id
from modules.places.places_controller import PlacesController


bp = Blueprint("places", __name__, url_prefix="/places")


@bp.post("/")
def create():
    payload = request.get_json()
    return PlacesController.create(payload)


@bp.patch("/")
@jwt_required()
def edit():
    payload = request.get_json()
    id = get_jwt_id()
    return PlacesController.edit(id, payload)


@bp.get("/")
@jwt_required()
def get_all():
    payload = request.get_json()
    return PlacesController.get(payload)


@bp.get("/<int:id>")
@jwt_required()
def get(id: int):
    return PlacesController.get_by_id(id)
