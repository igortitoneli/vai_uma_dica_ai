from typing import List, Optional

from flask import current_app
from common.exceptions.not_found_exception import NotFoundException
from modules.customers.customers_model import Customers
from modules.customers.dto.filter.customers_filter import CustomersFilter
from common.database import db
from modules.customers.dto.payload.customers_create import CustomersCreate
from modules.customers.dto.payload.customers_edit import CustomersEdit


class CustomersRepository:

    @classmethod
    def get_first(cls, filter: CustomersFilter) -> Customers:
        data = filter.model_dump(exclude_defaults=True, exclude_unset=True)
        query = db.session.query(Customers)
        for key, value in data.items():
            query = query.filter(getattr(Customers, key).in_(value))
        customer = query.first()
        if customer is None:
            raise NotFoundException("Customer not found.")
        return customer

    @classmethod
    def get_optional_first(cls, filter: CustomersFilter) -> Optional[Customers]:
        data = filter.model_dump(exclude_defaults=True, exclude_unset=True)
        query = db.session.query(Customers)
        for key, value in data.items():
            query = query.filter(getattr(Customers, key).in_(value))
        return query.first()

    @classmethod
    def get_all(cls, filter: CustomersFilter) -> List[Customers]:
        data = filter.model_dump(exclude_defaults=True, exclude_unset=True)
        query = db.session.query(Customers)
        for key, value in data.items():
            query = query.filter(getattr(Customers, key).in_(value))
        return query.all()

    @classmethod
    def create(cls, data: CustomersCreate) -> Customers:
        customer = Customers(
            name=data.name,
            email=data.email,
            password=data.password,
            phone=data.phone,
        )
        customer.save()
        return customer

    @classmethod
    def edit(cls, customer: Customers, data: CustomersEdit) -> Customers:
        json = data.model_dump(exclude_defaults=True, exclude_unset=True)
        for key, value in json.items():
            if hasattr(Customers, key) and key not in [
                "id",
                "created_at",
                "updated_at",
                "deleted_at",
            ]:
                current_app.logger.info(f"editando {key} - {value}")
                setattr(customer, key, value)
        customer.commit()
        return customer
