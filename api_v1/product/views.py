from fastapi import APIRouter, HTTPException, Depends
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper

from starlette import status

from . import crud
from .schemas import Product, ProductCreate

router = APIRouter(tags=["Products"])


@router.get("/", response_model=List[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session)


@router.get("/{product_id}", response_model=Product)
async def get_item_products(
    product_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    product = await crud.get_item_products(session=session, product_id=product_id)
    if product is not None:
        return product

    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Продукт не найден"
    )


@router.post("/", response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)
