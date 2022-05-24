import datetime
from typing import List, Optional
from models.category import Category, CategoryIn
from core.security import hash_password
from .base import BaseRepository
from db.category import category


class CategoryRepository(BaseRepository):
    async def get_all_parent(self) -> List[Category]:
        query = category.select().where(category.c.parent_id is None)
        return await self.database.fetch_all(query=query)

    async def get_by_parent_id(self, parent_id: int) -> List[Category]:
        query = category.select().where(category.c.parent_id == parent_id)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[Category]:
        query = category.select().where(category.c.id == id).first()
        item = await self.database.fetch_one(query=query)
        if item is None:
            return None
        return Category.parse_obj(item)

    async def create(self, c: CategoryIn) -> Category:
        item = Category(
            name=c.name,
            parent_id=c.parent_id
        )

        values = {**item.dict()}
        values.pop("id", None)
        query = category.insert().values(**values)
        item.id = await self.database.execute(query=query)
        return item

    async def update(self, id: int, c: Category) -> Category:
        item = Category(
            id=id,
            name=c.name,
        )

        values = {**item.dict()}
        values.pop("id", None)
        query = category.update().where(category.c.id == id).values(**values)
        await self.database.execute(query=query)
        return item

