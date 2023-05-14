from typing import List
from fastapi import APIRouter, Depends
from models.product import Product, ProductIn
from repositories.product import ProductRepository
from .depends import get_product_repository

router = APIRouter()


@router.get("/", response_model=List[Product])
async def product(category_id: int, products: ProductRepository = Depends(get_product_repository)):
    return await products.get_by_category(category_id)


@router.post("/", response_model=Product)
async def create_product(item: ProductIn, products: ProductRepository = Depends(get_product_repository)):
    return await products.create(c=item)

@router.put("/", response_model=Product)
async def update_product(id: int, item: Product, products: ProductRepository = Depends(get_product_repository)):
    return await products.update(id=id, c=item)


@router.get("/get_by_id", response_model=Product)
async def get_by_id(id: int, products: ProductRepository = Depends(get_product_repository)):
    return await products.get_by_id(id=id)


@router.delete("/delete")
async def delete(id: int, products: ProductRepository = Depends(get_product_repository)):
    return await products.delete(id=id)
