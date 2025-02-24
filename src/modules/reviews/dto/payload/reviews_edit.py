from typing import Optional
from pydantic import Field
from common.interfaces.dto.payload import PayloadInterface


class ReviewsEdit(PayloadInterface):
    id: Optional[int] = None
    customers_id: Optional[int] = None
    places_id: Optional[int] = None
    message: Optional[str] = None
    stars: Optional[int] = Field(default=None, ge=0, le=5)
