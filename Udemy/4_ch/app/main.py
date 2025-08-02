from fastapi import FastAPI

app = FastAPI()


# GET Request
# Read or fetch all data
@app.get("/product")
async def all_products():
    return {"response": "All products"}


# fetch single data
@app.get("/product/{product_id}")
async def single_product(product_id: int):
    return {
        "response": "fetch single data",
        "product_id": product_id,
    }


# POST Request
# Create data
@app.post("/product")
async def create_product(product_data: dict):
    return {
        "response": "Product created",
        "product_data": product_data,
    }


# PUT Request
# Update data
@app.put("/product/{product_id}")
async def update_product(new_updated_product: dict, product_id: int):
    return {
        "response": "Product created",
        "new_updated_product": new_updated_product,
        "product_id": product_id,
    }


# PUT Request
# Update partial data
@app.patch("/product/{product_id}")
async def update_partial_product(new_updated_product: dict, product_id: int):
    return {
        "response": "Partial product update",
        "new_updated_product": new_updated_product,
        "product_id": product_id,
    }


# Delete Request
# Delete data
@app.delete("/product/{product_id}")
async def delete_product(product_id: int):
    return {
        "response": "Delete the product",
        "product_id": product_id,
    }


def main():
    print("Hello from 4-ch!")


if __name__ == "__main__":
    main()
