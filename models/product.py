from pydantic import BaseModel, AnyUrl
from typing import Optional


class Product(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    image: Optional[AnyUrl] = None
    price: int
    category_id: int


class ProductIn(BaseModel):
    name: str
    description: str
    image: Optional[AnyUrl] = None
    price: int
    category_id: int
