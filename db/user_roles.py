import sqlalchemy
from .base import metadata

user_roles = sqlalchemy.Table(
    "user_roles",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column("role_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('roles.id')),
)
