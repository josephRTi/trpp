import sqlalchemy
from .base import metadata

roles = sqlalchemy.Table(
    "roles",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String, unique=True),
)
