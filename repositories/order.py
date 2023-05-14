import datetime

from databases.interfaces import Record

from models.order import OrderIn, Order
from .base import BaseRepository
from models.product import Product, ProductIn
from typing import List, Optional
from db.order import orders
from db.order_products import order_products


class OrderRepository(BaseRepository):

    async def get_orders(self) -> list[Record]:
        query = orders.select()
        return await self.database.fetch_all(query=query)

    async def get_by_user_id(self, user_id: int) -> list[Record]:
        query = orders.select().where(orders.c.user_id == user_id)
        return await self.database.fetch_all(query=query)

    async def get_info_by_id(self, id: int) -> list[Record]:
        query = f"SELECT * FROM order_products op JOIN product p ON p.id = op.product_id WHERE order_id = {id}"
        return await self.database.fetch_all(query=query)

    async def create(self, data):
        item = Order(
            user_id=data[b'user_id'],
            datetime=datetime.datetime.now()
        )

        values = {**item.dict()}
        values.pop("id", None)
        query = orders.insert().values(**values)
        item.id = await self.database.execute(query=query)

        for product in data[b'products']:
            d = {'order_id': item.id, 'product_id':product['id'], 'count':product['count']}
            query = order_products.insert().values(**d)
            await self.database.execute(query=query)
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
