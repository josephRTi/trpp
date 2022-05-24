from typing import List
from fastapi import APIRouter, Depends

import models.user
from models.category import CategoryIn, Category
from repositories.category import CategoryRepository
from .depends import get_category_repository

router = APIRouter()


@router.get("/", response_model=List[Category])
async def category(categories: CategoryRepository = Depends(get_category_repository)):
    return await categories.get_all_parent()


@router.post("/", response_model=Category)
async def create_category(item: CategoryIn, categories: CategoryRepository = Depends(get_category_repository)):
    return await categories.create(c=item)


@router.put("/", response_model=Category)
async def update_category(id: int, item: Category, categories: CategoryRepository = Depends(get_category_repository)):
    return await categories.update(id=id, c=item)


@router.get("/", response_model=Category)
async def get_child_categories(id: int, categories: CategoryRepository = Depends(get_category_repository)):
    return await categories.get_by_parent_id(parent_id=id)


@router.get("/", response_model=Category)
async def get_by_id(id: int, categories: CategoryRepository = Depends(get_category_repository)):
    return await categories.get_by_id(id=id)