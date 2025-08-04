from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

from typing import Annotated

app = FastAPI()


# Using field level example - using this way to set example values
class Category(BaseModel):
    name: str = Field(
        examples=["laptop"],
    )
    description: str = Field(
        examples=["product category"],
    )


# Using pydantic's json_schema_extra
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

    # Another way, but not useful
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 0,
                    "name": "mackbook air",
                    "price": 100.1,
                    "stock": 2,
                },
            ],
        },
    }


@app.post("/product")
async def create_product(
    product: Annotated[Product, Body(embed=True)],
    category: Annotated[Category, Body(embed=True)],
):
    return {"product": product, "category": category}
