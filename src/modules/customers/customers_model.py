from sqlalchemy import Integer, String
from common.date_mixin import DateMixin
from common.interfaces.model import Model
from sqlalchemy.orm import Mapped, mapped_column


class Customers(Model, DateMixin):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(45), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(60), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
