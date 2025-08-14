from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
)  # https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.sessionmaker

DATABASE_URL = "sqlite:///./sqlite.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
# expire_on_commit - without reloading access data
