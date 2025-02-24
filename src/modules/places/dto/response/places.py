from common.interfaces.dto.response import ResponseInterface


class PlacesResponse(ResponseInterface):
    id: int
    name: str
    latitude: float
    longitude: float
    address: str
