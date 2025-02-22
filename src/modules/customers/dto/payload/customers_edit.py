from typing import Optional
from common.interfaces.dto.payload import PayloadInterface
from common.types import EncodedPassword


class CustomersEdit(PayloadInterface):
    id: int
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[EncodedPassword] = None
    phone: Optional[str] = None
