from typing import List, Optional

from flask import current_app
from common.exceptions.not_found_exception import NotFoundException
from common.database import db
from modules.reviews.dto.filter.reviews_filter import ReviewsFilter
from modules.reviews.dto.payload.reviews_create import ReviewsCreate
from modules.reviews.dto.payload.reviews_edit import ReviewsEdit
from modules.reviews.reviews_model import Reviews


class ReviewsRepository:

    @classmethod
    def get_first(cls, filter: ReviewsFilter) -> Reviews:
        data = filter.model_dump(exclude_defaults=True, exclude_unset=True)
        query = db.session.query(Reviews)
        for key, value in data.items():
            query = query.filter(getattr(Reviews, key).in_(value))
        place = query.first()
        if place is None:
            raise NotFoundException("Place not found.")
        return place

    @classmethod
    def get_optional_first(cls, filter: ReviewsFilter) -> Optional[Reviews]:
        data = filter.model_dump(exclude_defaults=True, exclude_unset=True)
        query = db.session.query(Reviews)
        for key, value in data.items():
            query = query.filter(getattr(Reviews, key).in_(value))
        return query.first()

    @classmethod
    def get_all(cls, filter: ReviewsFilter) -> List[Reviews]:
        data = filter.model_dump(exclude_defaults=True, exclude_unset=True)
        query = db.session.query(Reviews)
        for key, value in data.items():
            query = query.filter(getattr(Reviews, key).in_(value))
        return query.all()

    @classmethod
    def create(cls, data: ReviewsCreate) -> Reviews:
        place = Reviews(
            places_id=data.places_id,
            customers_id=data.customers_id,
            message=data.message,
            stars=data.stars,
        )
        place.save()
        return place

    @classmethod
    def edit(cls, reviews: Reviews, data: ReviewsEdit) -> Reviews:
        json = data.model_dump(exclude_defaults=True, exclude_unset=True)
        for key, value in json.items():
            if hasattr(reviews, key) and key not in [
                "id",
                "created_at",
                "updated_at",
                "deleted_at",
            ]:
                current_app.logger.info(f"editando {key} - {value}")
                setattr(reviews, key, value)
        reviews.commit()
        return reviews
