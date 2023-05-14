from fastapi import APIRouter, Depends, HTTPException, status
from models.token import Token, Login
from repositories.roles import RoleRepository
from repositories.users import UserRepository
from core.security import verify_password, create_access_token
from .depends import get_user_repository, get_role_repository

router = APIRouter()


@router.post("/")
async def login(login: Login, users: UserRepository = Depends(get_user_repository), roles: RoleRepository = Depends(get_role_repository)):
    user = await users.get_by_email(login.email)
    user_roles = await roles.get_user_roles(int(user.id))
    is_admin = False
    for r in user_roles:
        if r['name'] == 'admin':
            is_admin = True
            break

    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверное имя пользователя или пароль")
    return Token(access_token=create_access_token({"sub": user.email}), token_type="Bearer"), user, is_admin
