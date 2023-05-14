from repositories.order import OrderRepository
from repositories.users import UserRepository
from repositories.roles import RoleRepository
from repositories.category import CategoryRepository
from repositories.product import ProductRepository
from db.base import database


def get_user_repository() -> UserRepository:
    return UserRepository(database)


def get_roles_repository() -> RoleRepository:
    return RoleRepository(database)


def get_category_repository() -> CategoryRepository:
    return CategoryRepository(database)


def get_product_repository() -> ProductRepository:
    return ProductRepository(database)


def get_role_repository() -> RoleRepository:
    return RoleRepository(database)


def get_order_repository() -> OrderRepository:
    return OrderRepository(database)
