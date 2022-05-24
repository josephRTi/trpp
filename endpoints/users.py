from typing import List
from fastapi import APIRouter, Depends

import models.user
from models.user import User, UserIn, UserOut
from repositories.users import UserRepository
from .depends import get_user_repository

router = APIRouter()


@router.get("/", response_model=List[UserOut])
async def read_users(limit: int = 100, skip: int = 0, users: UserRepository = Depends(get_user_repository)):
    return await users.get_all(limit=limit, skip=skip)


@router.post("/", response_model=UserOut)
async def create_user(user: UserIn, users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)


@router.put("/", response_model=UserOut)
async def update_user(id: int, user: UserIn, users: UserRepository = Depends(get_user_repository)):
    return await users.update(id=id, u=user)


