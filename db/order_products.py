import sqlalchemy
from .base import metadata

order_products = sqlalchemy.Table(
    "order_products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("order_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('orders.id')),
    sqlalchemy.Column("product_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('product.id')),
    sqlalchemy.Column("count", sqlalchemy.Integer)
)
