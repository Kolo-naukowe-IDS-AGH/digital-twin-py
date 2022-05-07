from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from app.db.models import Product


class EventType(str, Enum):
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"


class EventBase(BaseModel):
    info: str
    type: str

    x: str
    y: str

    created_at: datetime
    updated_at: datetime


class Event(EventBase):
    id: int
    product: Product

    class Config:
        orm_mode = True
