from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# Define an Enum class with allowed product categories
class ProductCategory(str, Enum):  # str - type, Enum is class type
    books = "books"
    mobile = "mobile"
    laptop = "laptop"


# Use the Enum as the type for the path paramaters
@app.get("/product/{category}")
async def get_products(category: ProductCategory):
    if category == ProductCategory.books:  # way 1
        return {"category": category, "message": "Books are awesome"}
    elif category.value == "mobile":  # way 2
        return {"category": category, "message": "mobile are awesome"}
    elif category == ProductCategory.laptop.value:
        return {"category": category, "message": "laptop  are awesome"}
    else:
        return {"message": "category not found"}
