import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from db.base import database
from endpoints import users, auth, roles, category, product, order

app = FastAPI(title="Shop")
origins = [
    "http://localhost",
    "http://localhost:8081",
    "http://127.0.0.1:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(roles.router, prefix="/role", tags=["role"])
app.include_router(category.router, prefix="/category", tags=["category"])
app.include_router(product.router, prefix="/product", tags=["product"])
app.include_router(order.router, prefix='/order', tags=["order"])


@app.on_event("startup")
async def startup():
    """initiating connecting with db"""
    await database.connect()


@app.on_event("shutdown")
async def shutdonw():
    """closing connection with db"""
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host="127.0.0.1", reload=True)

#docker-compose -f docker-compose.dev.yaml up
