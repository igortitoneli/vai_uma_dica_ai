from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from common.utils import datetime_now


class DateMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), insert_default=datetime_now, nullable=False
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    deleted_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
