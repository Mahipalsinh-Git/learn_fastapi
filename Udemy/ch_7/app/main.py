from fastapi import FastAPI
from enum import Enum


# Define an Enum class with allowed product categories
class ProductCategory(str, Enum):  # str - type, Enum is class type
    books = "books"
    mobile = "mobile"
    laptop = "laptop"


app = FastAPI()


# Use the Enum as the type for the path paramaters
@app.get("/product/{category}")
async def get_products(category: ProductCategory):
    return {"response": "product fetch", "category": category}
