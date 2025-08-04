from fastapi import FastAPI, Cookie
from pydantic import BaseModel

from typing import Annotated

app = FastAPI()


@app.get("/product/recommendations")
async def get_recommendations(session_id: Annotated[str | None, Cookie()] = None):
    if session_id:
        return {
            "message": f"Recommendations for session {session_id}",
            "session_id": session_id,
        }
    return {"message": "No data found"}


# To test this demo use below code in terminal, swagger not supported
# curl -H "Cookie: session_id=abcd" http://127.0.0.1:8000/product/recommendations
