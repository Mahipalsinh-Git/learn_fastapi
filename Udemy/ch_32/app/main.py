from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

app = FastAPI()


# Not most useful
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def get_items(
    item_id: int,
):  # if you pass as string then automatically raise the error
    return item_id
