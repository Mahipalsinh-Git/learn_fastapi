from fastapi import FastAPI


app = FastAPI()


# path paramaters
@app.get("/product/path_paramater/{product_id}")
async def single_product(
    product_id,
):  # not passed data type, which create issue and set by default as string
    return {
        "response": "fetch single data",
        "product_id": product_id,
    }


def main():
    print("Hello from ch-5!")


if __name__ == "__main__":
    main()
