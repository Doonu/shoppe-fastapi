from fastapi import APIRouter
from typing import List

from product import crud
from product.schemas import Product

router = APIRouter(prefix="/product", tags=["Product"])


@router.get("", response_model=List[Product])
def get_product(limit: int = 1, offset: int = 1):
    return crud.get_product(limit, offset)


@router.post("/{product_id}")
def change_product_price(product_id: int, new_price: int):
    return crud.change_product_price(product_id, new_price)


@router.post("")
def add_product(shop: List[Product]):
    return crud.add_product(shop)
