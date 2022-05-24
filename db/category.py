import sqlalchemy
from .base import metadata
import datetime

category = sqlalchemy.Table(
    "category",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("parent_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('category.id'), default=None),
    sqlalchemy.Column("name", sqlalchemy.String),
)
