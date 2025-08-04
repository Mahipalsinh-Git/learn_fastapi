from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    price: float | None = None


# Create or Insert data and access it
@app.post("/product")
async def create_product(new_product: Product):
    print("id:", new_product.id)
    return new_product


# Add new calculated attribute
@app.post("/product/calculated")
async def create_product_calculated(new_product: Product):
    product_dict = new_product.model_dump()
    price_with_tax = new_product.price + (new_product.price * 18 / 100)
    product_dict.update({"price_with_tax": price_with_tax})
    return product_dict


# Combining request body with path parameters
@app.put("/product/combine/{product_id}")
async def create_product_combine(product_id: int, new_product: Product):
    return {
        "product_id": product_id,
        "new_product": new_product,
    }


# Combining request body with query parameters
@app.put("/product/query/{product_id}")
async def create_product_query(
    product_id: int,
    new_product: Product,
    discount: float | None = None,
):
    return {
        "product_id": product_id,
        "new_product": new_product,
        "discount": discount,
    }
