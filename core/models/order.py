from datetime import datetime

from sqlalchemy import func, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .order_product import OrderProductAssociation


class Order(Base):
    promocode: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )

    products_details: Mapped[list["OrderProductAssociation"]] = relationship(
        back_populates="order"
    )
