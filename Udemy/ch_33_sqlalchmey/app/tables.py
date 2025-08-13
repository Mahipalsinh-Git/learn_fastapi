from db import engine
from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey

metaData = MetaData()

# user table
users = Table(
    "users",  # table name
    metaData,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
)

# post table / ONE-TO-MANY
posts = Table(
    "posts",
    metaData,
    Column("id", Integer, primary_key=True),
    Column(
        "user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    ),  # Set Foreign key, ONE-TO-MANY
    Column("title", String, nullable=False),
    Column("content", String, nullable=False),
)

# profile table / ONE-TO-ONE - Unique
profile = Table(
    "profile",
    metaData,
    Column("id", Integer, primary_key=True),
    Column(
        "user_id",
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    ),  # Set Foreign key
    Column("bio", String, nullable=False),
    Column("address", String, nullable=False),
)

# address table / MANY-TO-MANY - users have multiple address and multiple address belongs to multiple users
address = Table(
    "address",
    metaData,
    Column("id", Integer, primary_key=True),
    Column("street", String, nullable=False),
    Column("country", String, nullable=False),
)
# many to many association
user_address_association = Table(
    "user_address_association",
    metaData,
    Column(
        "user_id",
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "address_id",
        Integer,
        ForeignKey("address.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


# Create table in database
def create_table():
    metaData.create_all(engine)


# Drop table in database
def drop_table():
    metaData.drop_all(engine)
