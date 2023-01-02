from typing import Any, Optional, TypeVar, Generic
from fastapi_pagination.links import Page
from pydantic import BaseModel, Field

T = TypeVar("T")


class SubscriberBase(BaseModel):
    email: str


class SubscriberCreate(SubscriberBase):
    pass


class Subscriber(SubscriberBase):
    id: int

    class Config:
        orm_mode = True
