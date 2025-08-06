import os
import uuid
import shutil  # Handle multiple files

from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

# Upload file with Form data


# HTML form for testing
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
        <html>
            <body>
                <h2> User Profile Form </h2>
                <form action = "/user-with-file/" enctype="multipart/form-data" method="post">
                    <label for="username"> Username: </label>
                    <input type="text" id="username" name="username" required><br><br>
                    
                    <label for="file"> Profile Picture(optional): </label>
                    <input type="file" id="file" name="file" accept="image/*"><br><br>

                    <input type="submit" value="Upload">
                </form>
            </body>
        </html>
"""


@app.post("/user-with-file/")
async def create_user_with_file(
    username: Annotated[str, Form()],
    file: Annotated[UploadFile | None, File] = None,
):
    response = {"username": username}

    if file:
        save_path = f"upload/{file.filename}"
        os.makedirs("upload", exist_ok=True)

        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        response["filename"] = file.filename

    return response
