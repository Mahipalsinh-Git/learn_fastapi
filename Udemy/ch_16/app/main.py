from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

from typing import Annotated

app = FastAPI()


## Pydantic's field
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


@app.post("/product")
async def create_product(product: Product):
    return {"product": product}
