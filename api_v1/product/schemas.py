from pydantic import BaseModel, Field, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int = Field(..., gt=0)


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
