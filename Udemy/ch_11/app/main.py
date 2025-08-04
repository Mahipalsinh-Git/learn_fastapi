from fastapi import FastAPI, status

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


# GET Request
## Read or featch all data
@app.get("/products", status_code=status.HTTP_200_OK)
async def all_products():
    return {"response": PRODUCTS}


## Read or featch by id
@app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
async def get_product_by_id(product_id: int):
    # Way - 1
    #  return {
    #     "response": [product for product in PRODUCTS if product["id"] == product_id]
    # }

    # Way - 2
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product


# POST Request
## Create or Insert data
@app.post("/products", status_code=status.HTTP_201_CREATED)
async def create_product(new_product: dict):
    PRODUCTS.append(new_product)
    return {"response": "product addded successfully"}


# PUT Request
## Update data
@app.put("/product/{product_id}")
async def update_product(product_id: int, new_update_product: dict):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS[index] = new_update_product
    return {
        "status": "update",
        "product_id": product_id,
        "new updated product": new_update_product,
    }


# PATCH Request
## Update partial data
@app.put("/product/{product_id}")
async def partial_product(product_id: int, new_update_product: dict):
    for product in PRODUCTS:
        if product["id"] == product_id:
            product.update(new_update_product)
    return {
        "status": "partial updated",
        "product_id": product_id,
        "new updated product": new_update_product,
    }


# DELETE Request
## Delete data
@app.delete("/product/{product_id}")
async def partial_product(product_id: int):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS.pop(index)
    return {
        "status": "deleted",
        "message": "product deleted successfully",
    }
