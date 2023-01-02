from typing import Any, Optional

from pydantic import BaseModel, Field


class SubscriberBase(BaseModel):
    email: str


class SubscriberCreate(SubscriberBase):
    pass


class Subscriber(SubscriberBase):
    id: int

    class Config:
        orm_mode = True
