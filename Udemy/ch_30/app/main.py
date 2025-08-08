from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"apple": "red", "banana": "yellow"}


# Custom HTTPException
@app.get("/items/{item_id}")
async def get_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )
    return items[item_id]


# Custom Header HTTPException
@app.get("/items/header/{item_id}")
async def get_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"x-error-type": "missing item"},
        )
    return items[item_id]
