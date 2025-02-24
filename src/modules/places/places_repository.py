from typing import List, Optional

from flask import current_app
from common.exceptions.not_found_exception import NotFoundException
from common.database import db
from modules.places.dto.filter.places_filter import PlacesFilter
from modules.places.dto.payload.places_create import PlacesCreate
from modules.places.dto.payload.places_edit import PlacesEdit
from modules.places.places_model import Places


class PlacesRepository:

    @classmethod
    def get_first(cls, filter: PlacesFilter) -> Places:
        data = filter.model_dump(exclude_defaults=True, exclude_unset=True)
        query = db.session.query(Places)
        for key, value in data.items():
            query = query.filter(getattr(Places, key).in_(value))
        place = query.first()
        if place is None:
            raise NotFoundException("Place not found.")
        return place

    @classmethod
    def get_optional_first(cls, filter: PlacesFilter) -> Optional[Places]:
        data = filter.model_dump(exclude_defaults=True, exclude_unset=True)
        query = db.session.query(Places)
        for key, value in data.items():
            query = query.filter(getattr(Places, key).in_(value))
        return query.first()

    @classmethod
    def get_all(cls, filter: PlacesFilter) -> List[Places]:
        data = filter.model_dump(exclude_defaults=True, exclude_unset=True)
        query = db.session.query(Places)
        for key, value in data.items():
            query = query.filter(getattr(Places, key).in_(value))
        return query.all()

    @classmethod
    def create(cls, data: PlacesCreate) -> Places:
        place = Places(
            name=data.name,
            latitude=data.latitude,
            longitude=data.longitude,
            address=data.address,
        )
        place.save()
        return place

    @classmethod
    def edit(cls, Places: Places, data: PlacesEdit) -> Places:
        json = data.model_dump(exclude_defaults=True, exclude_unset=True)
        for key, value in json.items():
            if hasattr(Places, key) and key not in [
                "id",
                "created_at",
                "updated_at",
                "deleted_at",
            ]:
                current_app.logger.info(f"editando {key} - {value}")
                setattr(Places, key, value)
        Places.commit()
        return Places
