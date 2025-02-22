from datetime import datetime

from flask_jwt_extended import create_access_token
from common.config.token_config import TokenConfig
from modules.auth.auth_repository import AuthRepository
from modules.auth.dto.payload.login import LoginPayload
from modules.auth.dto.response.login import LoginResponse
from modules.customers.customers_repository import CustomerRepository
from modules.customers.dto.filter.customers_filter import CustomersFilter


class AuthService:

    @classmethod
    def login(cls, auth: LoginPayload) -> LoginResponse:
        customer = CustomerRepository.get_first(CustomersFilter(email=auth.email))
        AuthRepository.password_validation(customer, auth.password)

        token_time = TokenConfig().token_expiration
        token_expiration = datetime.now() + token_time

        additional_claims = AuthRepository.get_additional_claims(
            customer, token_expiration
        )

        access_token = create_access_token(
            identity=str(customer.id),
            expires_delta=token_time,
            additional_claims=additional_claims,
        )

        return LoginResponse(
            access_token=access_token,
            expires_in=int(token_expiration.timestamp()),
            name=customer.name,
        )
