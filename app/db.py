from sqlalchemy.ext.asyncio import create_async_engine

# DATABASE_URL = "sqlite:///./sqlite.db"
DATABASE_URL = "sqlite+aiosqlite://"

engine = create_async_engine(DATABASE_URL, echo=True)
