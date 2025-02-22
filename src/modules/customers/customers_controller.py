from typing import Any, Dict


from modules.customers.customers_service import CustomersService
from modules.customers.dto.payload.customers_create import CustomersCreate
from modules.customers.dto.payload.customers_edit import CustomersEdit


class CustomersController:

    @classmethod
    def create(cls, payload: Dict[str, Any]) -> Dict[str, Any]:
        data = CustomersCreate.model_validate(payload)
        response = CustomersService.create(data)
        return response.model_dump()

    @classmethod
    def edit(cls, id: int, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload["id"] = id
        data = CustomersEdit.model_validate(payload)
        response = CustomersService.edit(data)
        return response.model_dump()
