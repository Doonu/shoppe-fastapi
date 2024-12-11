from datetime import datetime

from sqlalchemy import func, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .order_product import Order_product_association

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .product import Product


class Order(Base):
    promocode: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )

    products: Mapped[list["Product"]] = relationship(
        secondary=Order_product_association, back_populates="order"
    )
