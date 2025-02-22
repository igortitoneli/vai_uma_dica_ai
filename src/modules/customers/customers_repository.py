from typing import List, Optional

from flask import current_app
from common.exceptions.not_found_exception import NotFoundException
from modules.customers.customers_model import Customer
from modules.customers.dto.filter.customers_filter import CustomersFilter
from common.database import db
from modules.customers.dto.payload.customers_create import CustomersCreate
from modules.customers.dto.payload.customers_edit import CustomersEdit


class CustomerRepository:

    @classmethod
    def get_first(cls, filter: CustomersFilter) -> Customer:
        data = filter.model_dump(exclude_defaults=True, exclude_unset=True)
        query = db.session.query(Customer)
        for key, value in data.items():
            query = query.filter(getattr(Customer, key).in_(value))
        customer = query.first()
        if customer is None:
            raise NotFoundException("Customer not found.")
        return customer

    @classmethod
    def get_optional_first(cls, filter: CustomersFilter) -> Optional[Customer]:
        data = filter.model_dump(exclude_defaults=True, exclude_unset=True)
        query = db.session.query(Customer)
        for key, value in data.items():
            query = query.filter(getattr(Customer, key).in_(value))
        return query.first()

    @classmethod
    def get_all(cls, filter: CustomersFilter) -> List[Customer]:
        data = filter.model_dump(exclude_defaults=True, exclude_unset=True)
        query = db.session.query(Customer)
        for key, value in data.items():
            query = query.filter(getattr(Customer, key).in_(value))
        return query.all()

    @classmethod
    def create(cls, data: CustomersCreate) -> Customer:
        customer = Customer(
            name=data.name,
            email=data.email,
            password=data.password,
            phone=data.phone,
        )
        customer.save()
        return customer

    @classmethod
    def edit(cls, customer: Customer, data: CustomersEdit) -> Customer:
        json = data.model_dump(exclude_defaults=True, exclude_unset=True)
        for key, value in json.items():
            if hasattr(Customer, key) and key not in [
                "id",
                "created_at",
                "updated_at",
                "deleted_at",
            ]:
                current_app.logger.info(f"editando {key} - {value}")
                setattr(customer, key, value)
        customer.commit()
        return customer
