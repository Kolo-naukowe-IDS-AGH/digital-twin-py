from datetime import datetime

from pydantic import BaseModel

from app.schema.events import Event


class ProductBase(BaseModel):
    info: str
    qr_code: str

    x: float
    y: float

    created_at: datetime
    updated_at: datetime


class Product(BaseModel):
    id: int
    events: list[Event]

    class Config:
        orm_mode = True
