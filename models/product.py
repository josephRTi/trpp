from pydantic import BaseModel, AnyUrl


class Product(BaseModel):
    id: int
    name: str
    description: str
    image: AnyUrl
    price: int
    category_id: int


class ProductIn(BaseModel):
    name: str
    description: str
    image: AnyUrl
    price: int
    category_id: int
