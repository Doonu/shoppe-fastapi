from sqlalchemy.orm import Mapped, relationship

from .base import Base
from .order_product import Order_product_association
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .order import Order


class Product(Base):
    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]

    orders: Mapped[list["Order"]] = relationship(
        secondary=Order_product_association, back_populates="product"
    )
