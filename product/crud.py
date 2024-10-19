from typing import List

from product.schemas import Product

fake_product_data = [
    {"id": 1, "title": "Кольцо", "price": 200_000},
    {"id": 2, "title": "Кольцо 3", "price": 210_000},
    {"id": 3, "title": "Кольцо", "price": 254_000},
    {"id": 4, "title": "Кольцо 2", "price": 20_000},
]


def get_product(limit: int, offset: int):
    return fake_product_data[offset - 1 :][:limit]


def change_product_price(product_id: int, new_price: int):
    current_shop = list(
        filter(lambda shop: shop.get("id") == product_id, fake_product_data)
    )[0]

    current_shop["price"] = new_price
    return {"statue": 200, "data": current_shop}


def add_product(shop: List[Product]):
    fake_product_data.extend(shop)
    return {"status": 200, "data": fake_product_data}
