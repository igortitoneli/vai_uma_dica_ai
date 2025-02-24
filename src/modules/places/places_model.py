from sqlalchemy import Float, Integer, String
from common.date_mixin import DateMixin
from common.interfaces.model import Model
from sqlalchemy.orm import Mapped, mapped_column


class Places(Model, DateMixin):
    __tablename__ = "places"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(45), nullable=False)
    latitude: Mapped[str] = mapped_column(Float, nullable=False)
    longitude: Mapped[str] = mapped_column(Float, nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
