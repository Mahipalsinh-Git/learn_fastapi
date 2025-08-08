from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()
fruits = {"apple": "red", "banana": "yellow"}


# Create Exception - exception class
class FruitException(Exception):
    def __init__(self, fruit_name: str):
        self.fruit_name = fruit_name


# Custom Exception Handler
@app.exception_handler(FruitException)
async def fruit_exception_handler(request: Request, exc: FruitException):
    return JSONResponse(
        status_code=404,
        content={"message": f"{exc.fruit_name} is not valid!"},
    )


@app.get("/fruit/{fruit_id}")
async def get_fruit(fruit_id: str):
    if fruit_id not in fruits:
        raise FruitException(fruit_name=fruit_id)
    return fruits[fruit_id]
