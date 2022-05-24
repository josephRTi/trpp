from fastapi import FastAPI
from db.base import database
import uvicorn
from endpoints import users, auth, roles, category

app = FastAPI(title="Shop")
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(roles.router, prefix="/role", tags=["role"])
app.include_router(category.router, prefix="/category", tags=["category"])



@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdonw():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host="127.0.0.1", reload=True)

#docker-compose -f docker-compose.dev.yaml up
