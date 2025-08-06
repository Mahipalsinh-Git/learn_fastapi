import os
import uuid
import shutil  # Handle multiple files

from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

# multipart/form-data


# HTML form for testing
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
        <html>
            <body>
                <h2> Single File Upload(bytes) </h2>
                <form action = "/files/" enctype="multipart/form-data" method="post">
                    <input name="file" type="file">
                    <input type="submit" value="Upload">
                </form>

                <br><br>

                <h2> Single File Upload(upload file) </h2>
                <form action = "/uploadfile/" enctype="multipart/form-data" method="post">
                    <input name="file" type="file">
                    <input type="submit" value="Upload">
                </form>

                <br><br>

                <h2> Multiple File Upload(upload multiple files) </h2>
                <form action = "/uploadmutiplefiles/" enctype="multipart/form-data" method="post">
                    <input name="multipleFiles" type="file" multiple>
                    <input type="submit" value="Upload">
                </form>
            </body>
        </html>
"""


@app.post("/files/")
async def create_file(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": "No file sent"}

    filename = f"{uuid.uuid4()}.bin"
    save_path = f"uploads/{filename}"

    os.makedirs("uploads", exist_ok=True)

    with open(save_path, "wb") as buffer:
        buffer.write(file)

    return {"message": "file saved"}


@app.post("/uploadfile/")
async def upload_file(file: Annotated[UploadFile | None, File()] = None):
    if not file:
        return {"message": "No file sent"}

    save_path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"{file.filename} - {file.content_type} saved"}


@app.post("/uploadmutiplefiles/")
async def upload_file(multipleFiles: Annotated[list[UploadFile] | None, File()] = None):
    if not multipleFiles:
        return {"message": "No file sent"}

    save_files = []
    os.makedirs("uploads", exist_ok=True)

    for file in multipleFiles:
        save_path = f"uploads/{file.filename}"
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        save_files.append({"filename": file.filename})

    return {"message": f"{file.filename} - {file.content_type} saved"}
