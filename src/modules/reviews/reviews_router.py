from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from common.utils import get_jwt_id
from modules.reviews.reviews_controller import ReviewsController


bp = Blueprint("reviews", __name__, url_prefix="/reviews")


@bp.post("/")
@jwt_required()
def create():
    payload = request.get_json()
    customers_id = get_jwt_id()
    return ReviewsController.create(customers_id, payload)


@bp.get("/")
@jwt_required()
def get():
    payload = request.get_json()
    return ReviewsController.get(payload)


@bp.get("/<int:id>/")
@jwt_required()
def get_by_id(id: int):
    return ReviewsController.get_by_id(id)
