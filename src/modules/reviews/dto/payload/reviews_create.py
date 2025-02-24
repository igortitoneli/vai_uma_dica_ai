from pydantic import Field
from common.interfaces.dto.payload import PayloadInterface


class ReviewsCreate(PayloadInterface):
    customers_id: int
    places_id: int
    message: str
    stars: float = Field(ge=0, le=5)
