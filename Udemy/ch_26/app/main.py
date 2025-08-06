from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

# Form type:
#   application/x-www-form-urlencoded
#   multipart/form-data


## Simple HTML form for testing
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <body>
            <h2> Login Form </h2>
            <form action="/login/" method="post">
                <label for="username"> Username: </label>
                <input type="text" id="username" name="username"><br><br>
                <label for="password"> Password: </label>
                <input type="text" id="password" name="password"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
"""


@app.post("/login/ ")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form(min_length=5)],
):
    return {"username": username, "password": password}
