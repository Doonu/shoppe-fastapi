from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int = Field(..., gt=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductUpdatePartial(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
