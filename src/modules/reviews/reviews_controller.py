from typing import Any, Dict

from modules.reviews.dto.filter.reviews_filter import ReviewsFilter
from modules.reviews.dto.payload.reviews_create import ReviewsCreate
from modules.reviews.dto.response.reviews import ReviewsResponse
from modules.reviews.reviews_service import ReviewsService


class ReviewsController:

    @classmethod
    def create(cls, customers_id: int, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload["customers_id"] = customers_id
        create_model = ReviewsCreate.model_validate(payload)
        review = ReviewsService.create(create_model)
        response_model = ReviewsResponse.from_model(review)
        return response_model.model_dump()

    @classmethod
    def get(cls, payload: Dict[str, Any]) -> Dict[str, Any]:
        create_model = ReviewsFilter.model_validate(payload)
        review_list = ReviewsService.get(create_model)
        response_model_list = [
            ReviewsResponse.from_model(place) for place in review_list
        ]
        return [response_model.model_dump() for response_model in response_model_list]

    @classmethod
    def get_by_id(cls, id: int) -> Dict[str, Any]:
        review = ReviewsService.get_by_id(id)
        response_model = ReviewsResponse.from_model(review)
        return response_model.model_dump()
