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

/