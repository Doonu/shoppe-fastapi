from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    title: str
    price: int = Field(..., gt=0)