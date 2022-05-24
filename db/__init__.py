from .users import users
from .roles import roles
from .user_roles import user_roles
from .category import category
from .base import metadata, engine

metadata.create_all(bind=engine)
