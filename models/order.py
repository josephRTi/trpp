from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Order(BaseModel):
    id: Optional[str] = None
    user_id: int
    datetime: datetime


class OrderIn(BaseModel):
    user_id: int

