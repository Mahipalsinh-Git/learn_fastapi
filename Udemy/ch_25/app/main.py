from fastapi import FastAPI
from pydantic import BaseModel

from typing import Annotated, Optional

app = FastAPI()

# Excludeing unset default values
products_db = {
    "1": {
        "id": "1",
        "name": "moto e",
        "price": 99.99,
        "stock": 1,
        "is_active": True,
    },
    "2": {
        "id": "1",
        "name": "lapton",
        "price": 9.99,
        "stock": 4,
        "is_active": False,
    },
}


class Product(BaseModel):
    id: str
    name: str
    price: float
    des: Optional[str] = None
    tax: float = 15.0


@app.get(
    "/products/{product_id}",
    response_model=Product,
    response_model_exclude_unset=True,
)
async def get_product(product_id: str):
    return products_db.get(product_id, {})


# specific field include
@app.get(
    "/products/field_include/{product_id}",
    response_model=Product,
    response_model_include={"name", "price"},
)
async def get_product_include_field(product_id: str):
    return products_db.get(product_id, {})


# specific field exclude
@app.get(
    "/products/field_exclude/{product_id}",
    response_model=Product,
    response_model_exclude={"name", "price", "tax "},
)
async def get_product_exclude_field(product_id: str):
    return products_db.get(product_id, {})
