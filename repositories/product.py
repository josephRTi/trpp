from .base import BaseRepository
from models.product import Product, ProductIn
from typing import List, Optional
from db.product import product


class ProductRepository(BaseRepository):
    async def get_by_category(self, category_id: int) -> List[Product]:
        query = product.select().where(product.c.category_id == category_id)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[Product]:
        query = product.select().where(product.c.id == id)
        item = await self.database.fetch_one(query=query)
        if item is None:
            return None
        return Product.parse_obj(item)

    async def create(self, c: ProductIn) -> Product:
        item = Product(
            name=c.name,
            description=c.description,
            image=c.image,
            price=c.price,
            category_id=c.category_id,
        )

        values = {**item.dict()}
        values.pop("id", None)
        query = product.insert().values(**values)
        item.id = await self.database.execute(query=query)
        return item

    async def update(self, id: int, c: Product) -> Product:
        item = Product(
            name=c.name,
            description=c.description,
            image=c.image,
            price=c.price,
            category_id=c.category_id,
        )

        values = {**item.dict()}
        values.pop("id", None)
        query = product.update().where(product.c.id == id).values(**values)
        await self.database.execute(query=query)
        return item

    async def delete(self, id: int):
        query = product.delete().where(product.c.id == id)
        await self.database.execute(query=query)
        return 200
