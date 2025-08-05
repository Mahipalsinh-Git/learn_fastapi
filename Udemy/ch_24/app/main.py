from fastapi import FastAPI
from pydantic import BaseModel

from typing import Annotated

app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None


class ProductOut(BaseModel):
    name: str
    price: float


# without return type
@app.get("/products")
async def get_products():
    return {"status": "ok"}


# With return and annotation
@app.get("/products/withReturnType", response_model=Product)
async def get_product_return():
    return {
        "id": 1,
        "name": "Moto E",
        "price": 33.10,
        "stock": 1,
    }
