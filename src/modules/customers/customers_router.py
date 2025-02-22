from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from common.utils import get_jwt_id
from modules.customers.customers_controller import CustomersController


bp = Blueprint("customers", __name__, url_prefix="/customers")


@bp.post("/")
def create():
    payload = request.get_json()
    return CustomersController.create(payload)


@bp.patch("/")
@jwt_required()
def edit():
    payload = request.get_json()
    id = get_jwt_id()
    return CustomersController.edit(id, payload)
