from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


# Form data using pydantic


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


# Pydantic model for Form
class UserData(BaseModel):
    username: str
    password: str


# @app.post("/login/")
# async def login(data: Annotated[UserData, Form()]):
#     return {"data": data}


# Pydantic model for Form with validation
class UserDataWithValidate(BaseModel):
    username: str = Field(max_length=15)
    password: str = Field(min_length=5)


@app.post("/login/")
async def login(data: Annotated[UserDataWithValidate, Form()]):
    return {"data": data}
