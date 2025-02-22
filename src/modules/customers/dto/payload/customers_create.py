from common.interfaces.dto.payload import PayloadInterface
from common.types import EncodedPassword


class CustomersCreate(PayloadInterface):
    name: str
    email: str
    password: EncodedPassword
    phone: str
