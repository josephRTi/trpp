import datetime
from typing import List, Optional

from asyncpg import Record

from models.roles import Role, RoleIn
from core.security import hash_password
from .base import BaseRepository
from db.roles import roles
from db.user_roles import user_roles


class RoleRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Record]:
        query = roles.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[Role]:
        query = roles.select().where(roles.c.id == id).first()
        role = await self.database.fetch_one(query=query)
        if role is None:
            return None
        return Role.parse_obj(role)

    async def get_user_roles(self, user_id: int) -> List[Record]:
        query = f"SELECT * FROM roles r JOIN user_roles ur ON r.id = ur.role_id WHERE user_id = {user_id};"
        return await self.database.fetch_all(query=query)

    async def create(self, r: RoleIn) -> Role:
        role = Role(
            name=r.name,
        )

        values = {**role.dict()}
        values.pop("id", None)
        query = roles.insert().values(**values)
        role.id = await self.database.execute(query=query)
        return role

    async def update(self, id: int, r: Role) -> Role:
        role = Role(
            id=id,
            name=r.name,
        )

        values = {**role.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        query = roles.update().where(roles.c.id == id).values(**values)
        await self.database.execute(query=query)
        return role

