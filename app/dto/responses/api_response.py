from typing import Any, Generic, List, Optional, TypeVar

from pydantic.generics import GenericModel

DataT = TypeVar('DataT')


class ApiResponse(GenericModel, Generic[DataT]):
    message: str | None = None
    status_code: int
    data: DataT | None = None
    error: List[str] = []
