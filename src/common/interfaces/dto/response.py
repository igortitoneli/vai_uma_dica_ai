from pydantic import BaseModel


class ResponseInterface(BaseModel):

    @classmethod
    def from_model(cls, obj: object):
        return cls.model_validate(obj, from_attributes=True)
