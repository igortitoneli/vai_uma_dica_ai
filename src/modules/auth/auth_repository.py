from datetime import datetime
from typing import Any, Dict
import bcrypt
from common.exceptions.unauthorized_exception import UnauthorizedException
from modules.customers.customers_model import Customers


class AuthRepository:

    @classmethod
    def password_validation(cls, customer: Customers, password: str):
        if not bcrypt.checkpw(password.encode(), customer.password.encode()):
            raise UnauthorizedException("Invalid user email or password. ")

    @staticmethod
    def get_additional_claims(
        customer: Customers, token_expiration: datetime
    ) -> Dict[str, Any]:
        return {
            "sub": str(customer.id),
            "exp": int(token_expiration.timestamp()),
            "name": customer.name,
        }
