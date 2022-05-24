import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr


class User(BaseModel):
    id: Optional[str] = None
    name: str
    surname: str
    middleName: str
    email: EmailStr
    hashed_password: str
    created_at: datetime.datetime


class UserIn(BaseModel):
    name: str
    surname: str
    middleName: str
    email: EmailStr
    password: constr(min_length=8)
    password2: str

    @validator("password2")
    def password_match(v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("Пароли не совпадают")
        return v


class UserOut(BaseModel):
    id: Optional[str] = None
    name: str
    surname: str
    middleName: str
    email: EmailStr
    created_at: datetime.datetime