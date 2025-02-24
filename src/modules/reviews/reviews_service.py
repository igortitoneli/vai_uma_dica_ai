from typing import List
from modules.customers.customers_repository import CustomersRepository
from modules.customers.dto.filter.customers_filter import CustomersFilter
from modules.places.dto.filter.places_filter import PlacesFilter
from modules.places.places_repository import PlacesRepository
from modules.reviews.dto.filter.reviews_filter import ReviewsFilter
from modules.reviews.dto.payload.reviews_create import ReviewsCreate
from modules.reviews.reviews_model import Reviews
from modules.reviews.reviews_repository import ReviewsRepository


class ReviewsService:

    @classmethod
    def create(cls, data: ReviewsCreate) -> Reviews:
        CustomersRepository.get_first(CustomersFilter(id=data.customers_id))
        PlacesRepository.get_first(PlacesFilter(id=data.places_id))
        return ReviewsRepository.create(data)

    @classmethod
    def get(cls, data: ReviewsFilter) -> List[Reviews]:
        return ReviewsRepository.get_all(data)

    @classmethod
    def get_by_id(cls, id: int) -> Reviews:
        return ReviewsRepository.get_first(ReviewsFilter(id=id))
