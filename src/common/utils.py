from datetime import datetime

from flask_jwt_extended import get_jwt_identity
from pytz import UTC


def datetime_now():
    return datetime.now(tz=UTC)


def get_jwt_id():
    return int(get_jwt_identity())
