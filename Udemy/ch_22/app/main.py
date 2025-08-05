from fastapi import FastAPI, Header
from pydantic import BaseModel

from typing import Annotated

app = FastAPI()


# Headers with a pydantic model
class ProductHeaders(BaseModel):
    authorization: str
    accept_language: str | None = None
    x_tracking_id: list[str] = []


@app.get("/products")
async def get_product(headers: Annotated[ProductHeaders, Header()]):
    return {"headers": headers}


# curl -H "Authorization: Bearer token123" -H "Accept-Language: en-US" -H "X-Tracking-Id: track1" -H "X-Tracking-Id: track2" http://127.0.0.1:8000/products


# Headers with a pydantic model with restrict header(forbidding extra heders)
class ProductHeadersForbid(BaseModel):
    model_config = {"extra": "forbid"}
    authorization: str
    accept_language: str | None = None
    x_tracking_id: list[str] = []


@app.get("/products/forbid")
async def get_product(headers: Annotated[ProductHeadersForbid, Header()]):
    return {"headers": headers}


# curl -H "Authorization: Bearer token123" -H "Accept-Language: en-US" -H "X-Tracking-Id: track1" -H "X-Tracking-Id: track2" -H "extra-header: extra" http://127.0.0.1:8000/products/forbid
