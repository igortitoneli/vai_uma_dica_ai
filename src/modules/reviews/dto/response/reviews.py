from common.interfaces.dto.response import ResponseInterface
from modules.customers.dto.response.cutomers import CustomersResponse
from modules.places.dto.response.places import PlacesResponse


class ReviewsResponse(ResponseInterface):
    id: int
    customers_id: int
    places_id: int
    message: str
    stars: float
    places: PlacesResponse
    customers: CustomersResponse
