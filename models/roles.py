from typing import Optional
from pydantic import BaseModel


class Role(BaseModel):
    id: Optional[str] = None
    name: str


class RoleIn(BaseModel):
    name: str
