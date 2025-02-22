from typing import Any, Optional

from flask import jsonify

from .api_exception import APIException


class ConflictException(APIException):
    def __init__(
        self,
        message: str,
        code: Optional[str] = None,
        payload: Optional[dict[str, Any]] = None,
        status_code=409,
    ) -> None:
        super().__init__(
            message=message, payload=payload, code=code, status_code=status_code
        )


def conflict_handler(exception: ConflictException):
    return jsonify(exception.to_dict()), exception.status_code
