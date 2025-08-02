from fastapi import FastAPI

app = FastAPI()


@app.get("/product")
async def get_all_products():
    return {"message": "product list"}
