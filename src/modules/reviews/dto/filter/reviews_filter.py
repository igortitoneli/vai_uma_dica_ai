from typing import Optional

from pydantic import Field
from common.interfaces.dto.filter import FilterInterface
from common.types import ToList


class ReviewsFilter(FilterInterface):
    id: Optional[ToList[int]] = None
    customers_id: Optional[ToList[int]] = None
    places_id: Optional[ToList[int]] = None
    message: Optional[ToList[str]] = None
    stars: Optional[ToList[str]] = Field(default=None, ge=0, le=5)
