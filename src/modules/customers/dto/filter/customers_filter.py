from typing import Optional
from common.interfaces.dto.filter import FilterInterface
from common.types import ToList


class CustomersFilter(FilterInterface):
    id: Optional[ToList[int]] = None
    name: Optional[ToList[str]] = None
    email: Optional[ToList[str]] = None
    phone: Optional[ToList[str]] = None
