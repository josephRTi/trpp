from typing import Optional
from pydantic import BaseModel


class Category(BaseModel):
    id: Optional[str] = None
    name: str
    parent_id: Optional[str] = None


class CategoryIn(BaseModel):
    name: str
    parent_id: Optional[str] = None

