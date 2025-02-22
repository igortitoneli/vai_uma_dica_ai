from common.interfaces.dto.response import ResponseInterface
from common.types import ToTimestamp


class LoginResponse(ResponseInterface):
    access_token: str
    expires_in: ToTimestamp
    name: str
    token_type: str = "Bearer"
