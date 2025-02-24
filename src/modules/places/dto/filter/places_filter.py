from typing import Optional
from common.interfaces.dto.filter import FilterInterface
from common.types import ToList


class PlacesFilter(FilterInterface):
    id: Optional[ToList[int]] = None
    name: Optional[ToList[str]] = None
    latitude: Optional[ToList[float]] = None
    longitude: Optional[ToList[float]] = None
    address: Optional[ToList[str]] = None
