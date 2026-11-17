from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class ServiceErrorModel(BaseModel, Generic[T]):
    code: int
    details: T