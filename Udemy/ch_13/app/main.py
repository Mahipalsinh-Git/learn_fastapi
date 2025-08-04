from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

PRODUCTS = [
    {
        "id": 1,
        "title": "first",
        "price": 100.10,
        "description": "first data",
    },
    {
        "id": 2,
        "title": "second",
        "price": 200.20,
        "description": "second data",
    },
    {
        "id": 3,
        "title": "third",
        "price": 300.30,
        "description": "third data",
    },
    {
        "id": 4,
        "title": "fourth",
        "price": 400.40,
        "description": "fourth data",
    },
]


# Basic
@app.get("/product/{product_id}")
async def get_products(product_id: int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return {"message": "data not found "}


# Numeric validation
@app.get("/product/validation/{product_id}")
async def get_products(product_id: Annotated[int, Path(ge=1)]):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return {"message": "data not found "}
