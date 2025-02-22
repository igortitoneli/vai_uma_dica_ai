from typing import Any, Dict

from modules.auth.auth_service import AuthService
from modules.auth.dto.payload.login import LoginPayload


class AuthController:

    @classmethod
    def login(cls, payload: Dict[str, Any]):
        auth = LoginPayload.model_validate(payload)
        response = AuthService.login(auth)
        return response.model_dump()
