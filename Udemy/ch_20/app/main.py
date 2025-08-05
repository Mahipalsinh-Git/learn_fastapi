from fastapi import FastAPI, Cookie, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


# Cookies with a pydantic model
class ProductCookies(BaseModel):
    session_id: str
    preferred_category: str | None = None
    tracking_id: str | None = None


@app.get("/product/recommendations")
async def get_recommendations(coockies: Annotated[ProductCookies, Cookie()]):
    response = {"session_id": coockies.session_id}
    if coockies.preferred_category:
        response["messages"] = (
            f"Recommendations for {coockies.preferred_category} products"
        )
    else:
        response["messages"] = (
            f"Default Recommendations for session {coockies.session_id}"
        )
    if coockies.tracking_id:
        response["tracking_id"] = coockies.tracking_id

    return response


# To test this demo use below code in terminal, swagger not supported
# curl -H "Cookie: session_id=abcd; preferred_category = Electronics; tracking_id = abcd" http://127.0.0.1:8000/product/recommendations


# Forbidding extra cookies - only model cookies allowed
class ProductCookiesForbid(BaseModel):
    model_config = {"extra": "forbid"}
    session_id: str
    preferred_category: str | None = None
    tracking_id: str | None = None


@app.get("/product/recommendations/forbid")
async def get_recommendations_forbid(
    forbidCoockies: Annotated[ProductCookiesForbid, Cookie()],
):
    response = {"session_id": forbidCoockies.session_id}
    if forbidCoockies.preferred_category:
        response["messages"] = (
            f"Recommendations for {forbidCoockies.preferred_category} products"
        )
    else:
        response["messages"] = (
            f"Default Recommendations for session {forbidCoockies.session_id}"
        )
    if forbidCoockies.tracking_id:
        response["tracking_id"] = forbidCoockies.tracking_id

    return response


# curl -H "Cookie: session_id=abcd; preferred_category = Electronics; tracking_id = abcd; extra-data=mydata" http://127.0.0.1:8000/product/recommendations/forbid
