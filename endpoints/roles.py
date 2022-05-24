from typing import List
from fastapi import APIRouter, Depends

import models.user
from models.roles import RoleIn, Role
from repositories.roles import RoleRepository
from .depends import get_roles_repository

router = APIRouter()


@router.get("/", response_model=List[Role])
async def read_roles(roles: RoleRepository = Depends(get_roles_repository)):
    return await roles.get_all()


@router.post("/", response_model=Role)
async def create_role(role: RoleIn, roles: RoleRepository = Depends(get_roles_repository)):
    return await roles.create(r=role)


@router.put("/", response_model=Role)
async def update_role(id: int, role: RoleIn, roles: RoleRepository = Depends(get_roles_repository)):
    return await roles.update(id=id, r=role)
