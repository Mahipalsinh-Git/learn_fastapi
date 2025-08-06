Package:
    uv add "fastapi[standard]"

Run the project :
    fastapi dev main.py         using fastapi command
    uvicorn main:app --reload   using uvicorn command

-------------------------
Folder structure
    horizontal 
    vertical - feature based structure
        - most useful
        - ddd(domain driven design)

    

    app
        __init__.py
        db - for database
            __init__.py
            config.py
        user - feature wise
            __init__.py
            models.py   - for models
            routes.py   - for api endpoints 
            schemas.py  - for pydantic models
            services.py - for business logic
            utils.py    -  for more extract if required

    test
        __init__.py
        user
            test_models.py
            test_routes.py
            test_services.py

-------------------------
Docs:
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc

-------------------------
    cd ..
    cd ..
    clear
    uv init ch_29
    cd ch_29
    mkdir app
    cd app     
    uv add "fastapi[standard]"

from fastapi import FastAPI
from pydantic import BaseModel

from typing import Annotated

app = FastAPI()

uvicorn main:app --reload