import json
from typing import List, Dict, Any, AnyStr, Union
from fastapi import APIRouter, Depends
from starlette.requests import Request

from models.order import Order, OrderIn
from models.product import Product, ProductIn
from repositories.order import OrderRepository
from repositories.product import ProductRepository
from .depends import get_order_repository

router = APIRouter()


@router.get("/", response_model=List[Order])
async def order(orders: OrderRepository = Depends(get_order_repository)):
    return await orders.get_orders()


JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]

@router.post("/")
async def create_order(arbitrary_json: JSONStructure = None, orders: OrderRepository = Depends(get_order_repository)):
    return await orders.create(arbitrary_json)


@router.get("/get_by_id")
async def get_by_id(id: int, orders: OrderRepository = Depends(get_order_repository)):
    return await orders.get_info_by_id(id=id)


@router.get("/get_by_user_id")
async def get_by_user_id(id: int, orders: OrderRepository = Depends(get_order_repository)):
    return await orders.get_by_user_id(user_id=id)
