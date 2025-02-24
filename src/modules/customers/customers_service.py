from common.exceptions.conflict import ConflictException
from modules.customers.customers_repository import CustomersRepository
from modules.customers.dto.filter.customers_filter import CustomersFilter
from modules.customers.dto.payload.customers_create import CustomersCreate
from modules.customers.dto.payload.customers_edit import CustomersEdit
from modules.customers.dto.response.cutomers import CustomersResponse


class CustomersService:

    @classmethod
    def create(cls, data: CustomersCreate) -> CustomersResponse:
        customer = CustomersRepository.get_optional_first(
            CustomersFilter(email=data.email)
        )
        if customer is not None:
            raise ConflictException("Customer already exists with this e-mail.")

        customer = CustomersRepository.create(data)
        return CustomersResponse.from_model(customer)

    @classmethod
    def edit(cls, data: CustomersEdit) -> CustomersResponse:
        customer = CustomersRepository.get_first(CustomersFilter(id=data.id))
        customer = CustomersRepository.edit(customer, data)
        return CustomersResponse.from_model(customer)
