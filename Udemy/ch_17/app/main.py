from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

from typing import Annotated

app = FastAPI()


# Nested body models
# Sub model
class Category(BaseModel):
    name: str = Field(
        title="Product name",
        description="The name of the product",
        max_length=15,
        min_length=3,
    )
    description: str = Field(
        title="Product description",
        description="The description of the product",
        max_length=15,
        min_length=3,
    )


# Model
class Product(BaseModel):
    id: int = 0
    name: str = Field(
        title="Product name",
        description="The name of the product",
        max_length=15,
        min_length=3,
        pattern="^[A-Za-z0-9]+$",
    )
    price: float = Field(
        title="Product price",
        description="The price of the product is must be greate than zero",
        gt=0,
    )
    stock: int | None = Field(
        default=None,
        title="Stock",
        description="The stock of the product is must be greate than zero",
        gt=0,
    )
    category: Category | None = Field(
        default=None,
        title="Product category",
        description="The category to which the product belongs",
    )


@app.post("/product")
async def create_product(product: Annotated[Product, Body(embed=True)]):
    return {"product": product}
