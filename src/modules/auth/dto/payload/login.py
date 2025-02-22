from common.interfaces.dto.payload import PayloadInterface


class LoginPayload(PayloadInterface):
    email: str
    password: str
