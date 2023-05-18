from typing import Any, Optional, TypeVar, Generic
from fastapi_pagination.links import Page
from pydantic import BaseModel, Field, EmailStr

T = TypeVar("T")


class SubscriberBase(BaseModel):
    email: EmailStr = Field(...)


class SubscriberCreate(SubscriberBase):
    pass


class Subscriber(SubscriberBase):
    id: int

    class Config:
        orm_mode = True
