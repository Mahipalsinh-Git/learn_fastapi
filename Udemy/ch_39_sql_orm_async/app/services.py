from models import User
from db import async_session
from sqlalchemy import Select, asc


# Insert / Create user
async def create_user(name: str, email: str):
    async with async_session() as session:
        user = User(name=name, email=email)
        session.add(user)
        await session.commit()
        return user


# Read use by ID
async def get_user_by_id(user_id: int):
    async with async_session() as session:
        user = await session.get_one(User, user_id)
        return user


async def get_all_users():
    async with async_session() as session:
        stmt = Select(User)
        users = await session.scalars(stmt)
        return users.all()


# update user email
async def update_user_email(user_id: int, new_email: str):
    async with async_session() as session:
        user = await session.get(User, user_id)
        if user:
            user.email = new_email
            await session.commit()
        return user


# Delete user
async def delete_user(user_id: int):
    async with async_session() as session:
        user = await session.get(User, user_id)
        if user:
            await session.delete(user)
            await session.commit()
