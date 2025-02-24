from typing import List
from modules.places.dto.filter.places_filter import PlacesFilter
from modules.places.dto.payload.places_create import PlacesCreate
from modules.places.dto.payload.places_edit import PlacesEdit
from modules.places.dto.response.places import PlacesResponse
from modules.places.places_model import Places
from modules.places.places_repository import PlacesRepository


class PlacesService:

    @classmethod
    def create(cls, data: PlacesCreate) -> Places:
        return PlacesRepository.create(data)

    @classmethod
    def edit(cls, data: PlacesEdit) -> Places:
        place = PlacesRepository.get_first(PlacesFilter(id=data.id))
        place = PlacesRepository.edit(place, data)
        return PlacesResponse.from_model(place)

    @classmethod
    def get(cls, filter: PlacesFilter) -> List[Places]:
        return PlacesRepository.get_all(filter)

    @classmethod
    def get_by_id(cls, id: int) -> Places:
        return PlacesRepository.get_first(PlacesFilter(id=id))
