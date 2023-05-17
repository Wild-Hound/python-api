from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from datetime import datetime

T = TypeVar("T")


class UserSchema(BaseModel):
    id: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None
    full_name: Optional[str] = None
    age: Optional[int] = None
    created: Optional[datetime]

    class Config:
        orm_mode = True


class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)


class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
