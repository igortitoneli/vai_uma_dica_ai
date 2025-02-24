from datetime import datetime
from typing import Any, Dict, List

from flask import request
from flask_jwt_extended import get_jwt_identity
from pytz import UTC


def datetime_now():
    return datetime.now(tz=UTC)


def get_jwt_id():
    return int(get_jwt_identity())


def get_params() -> Dict[str, List[Any]]:
    json: Dict[str, List[Any]] = {}
    for key, value in request.args.items():
        json[key] = value.split(",")
    return json
