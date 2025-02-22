from datetime import datetime
from typing import Any, Dict
import bcrypt
from common.exceptions.unauthorized_exception import UnauthorizedException
from modules.customers.customers_model import Customer


class AuthRepository:

    @classmethod
    def password_validation(cls, customer: Customer, password: str):
        if not bcrypt.checkpw(password.encode(), customer.password.encode()):
            raise UnauthorizedException("Invalid user email or password. ")

    @staticmethod
    def get_additional_claims(
        customer: Customer, token_expiration: datetime
    ) -> Dict[str, Any]:
        return {
            "sub": str(customer.id),
            "exp": int(token_expiration.timestamp()),
            "name": customer.name,
        }
