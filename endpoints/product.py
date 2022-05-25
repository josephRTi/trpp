from typing import List
from fastapi import APIRouter, Depends
from models.product import Product, ProductIn
from repositories.product import ProductRepository
from .depends import get_product_repository

router = APIRouter()


@router.get("/", response_model=List[Product])
async def category(category_id: int, categories: ProductRepository = Depends(get_product_repository)):
    return await categories.get_by_category(category_id)


@router.post("/", response_model=Product)
async def create_category(item: ProductIn, categories: ProductRepository = Depends(get_product_repository)):
    return await categories.create(c=item)


@router.put("/", response_model=Product)
async def update_category(id: int, item: Product, categories: ProductRepository = Depends(get_product_repository)):
    return await categories.update(id=id, c=item)


@router.get("/", response_model=Product)
async def get_by_id(id: int, products: ProductRepository = Depends(get_product_repository)):
    return await products.get_by_id(id=id)
