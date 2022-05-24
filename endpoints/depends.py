from repositories.users import UserRepository
from repositories.roles import RoleRepository
from repositories.category import CategoryRepository
from db.base import database


def get_user_repository() -> UserRepository:
    return UserRepository(database)


def get_roles_repository() -> RoleRepository:
    return RoleRepository(database)


def get_category_repository() -> CategoryRepository:
    return CategoryRepository(database)
