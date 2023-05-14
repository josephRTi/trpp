from .users import users
from .roles import roles
from .user_roles import user_roles
from .category import category
from .product import product
from .order import orders
from .order_products import order_products
from .base import metadata, engine

metadata.create_all(bind=engine)
