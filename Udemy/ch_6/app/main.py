from fastapi import FastAPI


app = FastAPI()


# Orders matters


@app.get("/product/temp_product_data")
async def single_product_static():
    return {
        "response": "single_product_static",
    }


@app.get("/product/{product_title}")
async def single_product(
    product_title: str,
):
    return {
        "response": "fetch single data",
        "product_title": product_title,
    }


# Note: if this function write below then it not calling due to orders, for that, this function set above one
# @app.get("/product/temp_product_data")
# async def single_product_static():
#     return {
#         "response": "single_product_static",
#     }


def main():
    print("Hello from ch-5!")


if __name__ == "__main__":
    main()
