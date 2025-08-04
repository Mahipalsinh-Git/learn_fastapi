from fastapi import FastAPI, Body
from pydantic import BaseModel

from typing import Annotated

app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None


class Seller(BaseModel):
    username: str
    full_name: str | None = None


@app.post("/product")
async def create_product(product: Product, seller: Seller):
    return {"product": product, "seller": seller}


# Make body optional
@app.post("/product/optional")
async def create_product_optional(product: Product, seller: Seller | None = None):
    return {"product": product, "seller": seller}


# Singular value in body
@app.post("/product/singular")
async def create_product_singular(
    product: Product,
    seller: Seller,
    sec_key: Annotated[str, Body()],  # Pass extra value in body
):
    return {"product": product, "seller": seller, "sec_key": sec_key}


## Embed
# Without embed - there is no class name as key in body
@app.post("/product/without_embed")
async def create_product_without_embed(product: Product):
    return {"product": product}


# Ex. Without embed
# {
#   "id": 0,
#   "name": "string",
#   "price": 0,
#   "stock": 0
# }


# With embed - there is class name as key in body
@app.post("/product/with_embed")
async def create_product_embed(product: Annotated[Product, Body(embed=True)]):
    return {"product": product}


# Ex. With embed
# {
#     "product": {
#         "id": 0,
#         "name": "string",
#         "price": 0,
#         "stock": 0,
#     },
# }
