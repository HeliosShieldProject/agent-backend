from typing import TypeVar, Generic, Optional
from app.core.enums import Error
from pydantic import BaseModel

T = TypeVar("T")


class Response(BaseModel, Generic[T]):
    data: Optional[T] = None
    error: Optional[Error] = None
