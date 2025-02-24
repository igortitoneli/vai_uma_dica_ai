from typing import Any, Dict


from modules.places.dto.filter.places_filter import PlacesFilter
from modules.places.dto.payload.places_create import PlacesCreate
from modules.places.dto.payload.places_edit import PlacesEdit
from modules.places.dto.response.places import PlacesResponse
from modules.places.places_service import PlacesService


class PlacesController:

    @classmethod
    def create(cls, payload: Dict[str, Any]) -> Dict[str, Any]:
        data = PlacesCreate.model_validate(payload)
        place = PlacesService.create(data)
        response_model = PlacesResponse.from_model(place)
        return response_model.model_dump()

    @classmethod
    def edit(cls, id: int, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload["id"] = id
        data = PlacesEdit.model_validate(payload)
        place = PlacesService.edit(data)
        response_model = PlacesResponse.from_model(place)
        return response_model.model_dump()

    @classmethod
    def get(cls, payload: Dict[str, Any]) -> Dict[str, Any]:
        data = PlacesFilter.model_validate(payload)
        place_list = PlacesService.get(data)
        response_model_list = [PlacesResponse.from_model(place) for place in place_list]
        return [response_model.model_dump() for response_model in response_model_list]

    @classmethod
    def get_by_id(cls, id: int) -> Dict[str, Any]:
        place = PlacesService.get_by_id(id)
        response_model = PlacesResponse.from_model(place)
        return response_model.model_dump()
