from sqlalchemy import Float, ForeignKey, Integer, Text
from common.date_mixin import DateMixin
from common.interfaces.model import Model
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.customers.customers_model import Customers
from modules.places.places_model import Places


class Reviews(Model, DateMixin):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    places_id: Mapped[str] = mapped_column(
        Integer, ForeignKey("places.id"), nullable=False
    )
    customers_id: Mapped[str] = mapped_column(
        Integer, ForeignKey("customers.id"), nullable=False
    )
    message: Mapped[str] = mapped_column(Text, nullable=False)
    stars: Mapped[str] = mapped_column(Float, nullable=False)

    places: Mapped[Places] = relationship(Places)
    customers: Mapped[Customers] = relationship(Customers)
