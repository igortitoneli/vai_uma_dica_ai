from typing import Any, Optional

from flask import jsonify

from .api_exception import APIException


class UnauthorizedException(APIException):
    def __init__(
        self,
        message: str = "",
        code: Optional[str] = None,
        payload: Optional[dict[str, Any]] = None,
    ) -> None:
        super().__init__(message=message, code=code, status_code=401, payload=payload)


def unauthorized_exception_handler(exception: UnauthorizedException):
    return jsonify(exception.to_dict()), exception.status_code
