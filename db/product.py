import sqlalchemy
from .base import metadata
import datetime

product = sqlalchemy.Table(
    "product",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Float),
    sqlalchemy.Column("category_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('category.id')),
)
