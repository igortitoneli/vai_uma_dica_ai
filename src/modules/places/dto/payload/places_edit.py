from typing import Optional
from common.interfaces.dto.payload import PayloadInterface


class PlacesEdit(PayloadInterface):
    id: int
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    address: Optional[str] = None
