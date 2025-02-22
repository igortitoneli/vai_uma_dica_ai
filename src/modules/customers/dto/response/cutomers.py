from common.interfaces.dto.response import ResponseInterface


class CustomersResponse(ResponseInterface):
    id: int
    name: str
    email: str
    phone: str
