from fastapi import FastAPI
from pydantic import BaseModel

from typing import Annotated, List

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
@app.get("/products/withReturnType")
async def get_product_return() -> Product:
    return {
        "id": 1,
        "name": "Moto E",
        "price": 33.10,
        "stock": 1,
    }


# With extra param - not working
@app.get("/products/withextrapara")
async def get_product_with_extra_para() -> Product:
    return {
        "id": 1,
        "name": "Moto E",
        "price": 33.10,
        "stock": 1,
        "desc": "this is new phone",
    }


# With return and annotation
@app.get("/products/withReturnList")
async def get_product_return_list() -> List[Product]:
    return [
        {"id": 1, "name": "Moto E", "price": 33.10, "stock": 1},
        {"id": 2, "name": "Moto G", "price": 35.99, "stock": 5},
    ]


# With post return type
@app.post("/products/withPost")
async def get_post(product: Product) -> Product:
    return product


# With some data
@app.post("/products/withSomeData")
async def get_with_somedata(product: Product) -> ProductOut:
    return product


## Create user
class BaseUser(BaseModel):
    username: str
    full_name: str | None = None


class UserIn(BaseUser):  # Inheritance
    password: str


@app.post("/create_user")
async def createUser(user: UserIn) -> BaseUser:
    return user
