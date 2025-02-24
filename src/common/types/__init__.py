from datetime import datetime
from enum import Enum
from typing import Annotated, Any, Generic, List, Type, TypeVar

import bcrypt
from pydantic import AfterValidator, BeforeValidator

T = TypeVar("T")


def to_timestamp(value: Any):
    if isinstance(value, datetime):
        return int(value.timestamp())
    return value


def encode_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


ToTimestamp = Annotated[int, BeforeValidator(to_timestamp)]

EncodedPassword = Annotated[str, AfterValidator(encode_password)]


class ToList(Generic[T]):
    """Classe para validar e transformar valores em listas do tipo especificado"""

    @classmethod
    def __class_getitem__(cls, expected_type: Type[T]):
        """
        Permite a sintaxe `ListOf[int]`, `ListOf[str]`, etc.
        Retorna um `Annotated` diretamente, sem precisar de `()`.
        """
        return Annotated[
            List[expected_type], BeforeValidator(cls._validate(expected_type))
        ]

    @staticmethod
    def _validate(expected_type: Type[T]):
        """Retorna a função de validação"""

        def validate(value) -> List[T]:
            # Se for um Enum, validamos strings compatíveis
            if issubclass(expected_type, Enum):

                def convert_to_enum(item):
                    if isinstance(item, expected_type):  # Já é um Enum
                        return item
                    if (
                        isinstance(item, str)
                        and item in expected_type.__members__.values()
                    ):
                        return expected_type(item)  # Converte string para Enum
                    raise TypeError(
                        f"Valor '{item}' inválido. Deve ser um dos {list(expected_type)}"
                    )

                if isinstance(value, list):
                    return [convert_to_enum(item) for item in value]
                return [convert_to_enum(value)]  # Converte item único para lista

            # Validação normal para tipos não-Enum
            if isinstance(value, list):
                if all(
                    isinstance(expected_type(item), expected_type) for item in value
                ):
                    return value
                raise TypeError(
                    f"Todos os elementos da lista devem ser do tipo {expected_type.__name__}"
                )

            if isinstance(value, expected_type):
                return [value]  # Transforma um único item no tipo esperado em uma lista

            raise TypeError(
                f"Valor deve ser do tipo {expected_type.__name__} ou uma lista contendo apenas esse tipo"
            )

        return validate
