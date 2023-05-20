from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from datetime import datetime

T = TypeVar("T")


class UrlSchema(BaseModel):
    main_url: str
    redirect_url: str

    class Config:
        orm_mode = True


class RequestUrl(BaseModel):
    parameter: UrlSchema = Field(...)


class Response (GenericModel, Generic[T]):
    code: str
    message: str
    result: Optional[T]
