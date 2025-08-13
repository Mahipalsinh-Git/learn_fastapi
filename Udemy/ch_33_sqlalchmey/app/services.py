from db import engine
from tables import users, posts
from sqlalchemy import insert, select, update, delete, asc, desc, func, text


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


# Get all users Ordered by name (A-Z)
def get_users_ordered_by_name():
    with engine.connect() as conn:
        stmt = select(users).order_by(asc(users.c.name))
        result = conn.execute(stmt).fetchall()
        return result


# Get all posts ordered by latest
def get_post_latest_first():
    with engine.connect() as conn:
        stmt = select(posts).order_by(desc(posts.c.id))
        result = conn.execute(stmt).fetchall()
        return result


# Group posts by user(count how many posts each user has)
def get_post_count_per_user():
    with engine.connect() as conn:
        stmt = select(
            posts.c.user_id, func.count(posts.c.id).label("total_posts")
        ).group_by(posts.c.user_id)

        result = conn.execute(stmt).fetchall()
        return result


# Join users and posts (list all posts with author names)
def get_posts_with_author():
    with engine.connect() as conn:
        stmt = select(
            posts.c.id,
            posts.c.title,
            users.c.name.label("author_name"),
        ).join(users, posts.c.user_id == users.c.id)

        result = conn.execute(stmt).fetchall()
        return result


# ------------- Using Raw query -------------
def raw_sql_insert_full_query(user_insert_query: str):
    with engine.connect() as conn:
        stmt = text(user_insert_query)
        conn.execute(stmt)
        conn.commit()


def raw_sql_insert_values(name: str, email: str):
    with engine.connect() as conn:
        stmt = text(
            """
            INSERT INTO users(name, email)
            VALUES(:name, :email)     
        """
        )
        conn.execute(stmt, {"name": name, "email": email})
        conn.commit()


def raw_sql_select(email: str):
    with engine.connect() as conn:
        stmt = text("SELECT * FROM users WHERE email = :email")
        result = conn.execute(stmt, {"email": email}).fetchall()
        return result
