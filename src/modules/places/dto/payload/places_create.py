from common.interfaces.dto.payload import PayloadInterface


class PlacesCreate(PayloadInterface):
    name: str
    latitude: float
    longitude: float
    address: str
