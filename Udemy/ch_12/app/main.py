from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import AfterValidator

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


# Normal way - Basic query paramater
@app.get("/products")
async def get_products(search: str | None = None):
    if search:
        search_lower = search.lower()
        filered_products = []

        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filered_products.append(product)
        return filered_products
    return PRODUCTS


# Validation without annotated - old way - not recent use
@app.get("/products/query")
async def get_products_with_query(
    search: str | None = Query(
        default=None,
        max_length=3,
    )
):
    if search:
        search_lower = search.lower()
        filered_products = []

        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filered_products.append(product)
        return filered_products
    return PRODUCTS


# Validation with annotated - most useful way
@app.get("/products/annotated")
async def get_products_with_annotated(
    search: Annotated[str | None, Query(max_length=3)] = None,
):
    if search:
        search_lower = search.lower()
        filered_products = []

        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filered_products.append(product)
        return filered_products
    return PRODUCTS


# Required paramaters
@app.get("/products/required")
async def get_products_with_required(
    search: Annotated[str, Query(max_length=3)],
):
    if search:
        search_lower = search.lower()
        filered_products = []

        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filered_products.append(product)
        return filered_products
    return PRODUCTS


# Regular expression
@app.get("/products/expression")
async def get_products_with_expression(
    search: Annotated[str, Query(max_length=3, pattern="^[a-z]+$")] = None,
):
    if search:
        search_lower = search.lower()
        filered_products = []

        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filered_products.append(product)
        return filered_products
    return PRODUCTS


# Multiples search temrs(List)
@app.get("/products/multiplesearch")
async def get_products_with_multiple_search(
    search: Annotated[list[str], Query()] = None,
):
    if search:
        filered_products = []

        for product in PRODUCTS:
            for s in search:
                if s.lower() in product["title"].lower():
                    filered_products.append(product)
        return filered_products
    return PRODUCTS


# Regular alias
@app.get("/products/alias")
async def get_products_with_alias(
    search: Annotated[str, Query(alias="find")] = None,
):
    if search:
        search_lower = search.lower()
        filered_products = []

        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filered_products.append(product)
        return filered_products
    return PRODUCTS


# Regular metadata
@app.get("/products/metadata")
async def get_products_with_metadata(
    search: Annotated[
        str, Query(alias="find", title="find products", description="search by product")
    ] = None,
):
    if search:
        search_lower = search.lower()
        filered_products = []

        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filered_products.append(product)
        return filered_products
    return PRODUCTS


# Deprecated
@app.get("/products/deprecated")
async def get_products_with_deprecated(
    search: Annotated[str, Query(deprecated=True)] = None,
):
    if search:
        search_lower = search.lower()
        filered_products = []

        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filered_products.append(product)
        return filered_products
    return PRODUCTS


# Custom validation
def check_valid_id(id: str):
    if not id.startswith("prod-"):
        raise ValueError("ID must start with 'prod-'")
    return id


@app.get("/products/customvalidation")
async def get_products_with_customvalidation(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        return {"id": id, "message": "valid product id"}
    return {"message": "No ID provided "}
