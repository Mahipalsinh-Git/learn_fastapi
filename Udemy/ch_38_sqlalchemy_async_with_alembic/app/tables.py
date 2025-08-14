from db import engine
from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey
import asyncio

metaData = MetaData()

# user table
users = Table(
    "users",  # table name
    metaData,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
)

# There is no requirements due to alembic
# async def create_table():
#     async with engine.begin() as conn:
#         await conn.run_sync(metaData.create_all)


# async def drop_table():
#     async with engine.begin() as conn:
#         await conn.run_sync(metaData.drop_all)
