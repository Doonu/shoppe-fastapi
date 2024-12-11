from sqlalchemy import Table, ForeignKey, Column, Integer, UniqueConstraint
from .base import Base

Order_product_association = Table(
    "order_product_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", ForeignKey("order.id"), nullable=False, unique=True),
    Column("product_id", ForeignKey("product.id"), nullable=False, unique=True),
    UniqueConstraint("order_id", "product_id", name="id_unique_order_product"),
)
