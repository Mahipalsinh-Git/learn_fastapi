from db import engine
from tables import users, posts
from sqlalchemy import insert, select, update, delete


# Insert or Create User
def create_user(name: str, email: str):
    with engine.connect() as conn:
        stmt = insert(users).values(
            name=name, email=email
        )  # insert values into column name

        conn.execute(stmt)  # statement execute
        conn.commit()  # commit the data into database, if this line is not written the data not store


# Insert or Create Posts
def create_post(user_id: int, title: str, content: str):
    with engine.connect() as conn:
        stmt = insert(posts).values(
            user_id=user_id,
            title=title,
            content=content,
        )  # insert values into column name

        conn.execute(stmt)  # statement execute
        conn.commit()  # commit the data into database, if this line is not written the data not store


# Get user by id
def get_user_by_id(user_id: int):
    with engine.connect() as conn:
        stmt = select(users).where(users.c.id == user_id)
        result = conn.execute(stmt).first()  # return single record
        return result


# Get post by user id
def get_posts_by_user_id(user_id: int):
    with engine.connect() as conn:
        stmt = select(posts).where(posts.c.user_id)  # foreign key
        result = conn.execute(stmt).fetchall()  # return multiple records
        return result


# Get all post
def get_all_posts():
    with engine.connect() as conn:
        stmt = select(posts)
        result = conn.execute(stmt).fetchall()  # return multiple records
        return result


# update user email
def update_user_email(user_id: int, new_email: str):
    with engine.connect() as conn:
        stmt = update(users).where(users.c.id == user_id).values(email=new_email)
        conn.execute(stmt)
        conn.commit()


# Delete post
def delete_post(post_id: int):
    with engine.connect() as conn:
        stmt = delete(posts).where(posts.c.id == post_id)
        conn.execute(stmt)
        conn.commit()
