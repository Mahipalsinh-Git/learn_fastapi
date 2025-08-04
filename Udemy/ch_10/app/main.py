from fastapi import FastAPI

app = FastAPI()


# Query paramater
@app.get("/product")
async def product(category: str, title: str):  # passing arguments as query paramaters
    return {"status": "Ok", "category": category, "title": title}


# Query paramater with default value
@app.get("/product/default")
async def product_with_default(
    category: str, limit: int = 10
):  # passing arguments as query paramaters
    return {"status": "Ok", "category": category, "limit": limit}


# Query paramater with optional value
@app.get("/product/optional")
async def product_with_optional(
    limit: int, category: str | None = None
):  # passing arguments as query paramaters
    return {"status": "Ok", "category": category, "limit": limit}


# Query paramater with path paramater
@app.get("/product/withpath/{year}")
async def product_with_path_paramater(
    category: str, year: str
):  # passing arguments as query paramaters
    return {"status": "Ok", "category": category, "year": year}
