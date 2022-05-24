from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("DATABASE_URL", cast=str, default="")

ACCESS_TOKEN_EXPIRE_MINUTES = 60

ALGORITHM = "HS256"
SECRET_KEY = config("SECRET_KEY", cast=str, default="64626c883dbbbb28115be8094a16a969fe5fe5bd005e60ce114b00026806a5b4")