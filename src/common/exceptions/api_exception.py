from typing import Any, Optional

from flask import jsonify

from . import http_status_code_to_error_code


class APIException(Exception):
    def __init__(
        self,
        message: str,
        code: Optional[str] = None,
        status_code: int = 400,
        payload: Optional[dict[str, Any]] = None,
    ) -> None:
        code = code if code is not None else http_status_code_to_error_code(status_code)

        self.message = message
        self.code = code
        self.status_code = status_code
        self.payload = payload

        super().__init__(message, code, status_code, payload)

    def to_dict(self) -> dict[str, Any]:
        dict_repr = self.payload or {}
        dict_repr["message"] = self.message
        dict_repr["status"] = self.code
        return dict_repr


def api_exception_handler(exception: APIException):
    return jsonify(exception.to_dict()), exception.status_code
