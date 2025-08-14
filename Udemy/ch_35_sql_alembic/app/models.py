from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey

from db import engine


class Base(DeclarativeBase):
    pass


# User Model/User Table
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)  # String length is 50
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(Integer, unique=True)

    # One-to-Many: User to post
    posts: Mapped[list["Post"]] = relationship(
        "Post",
        back_populates="user",
        cascade="all, delete",
    )

    # One-to-One: User to profile
    profile: Mapped["Profile"] = relationship(
        "Profile",
        back_populates="user",
        cascade="all, delete",
        uselist=False,  # Verify there is no list
    )

    # Many-to-Many: User to address
    address: Mapped[list["Address"]] = relationship(
        "Address",
        back_populates="user",
        cascade="all, delete",
    )

    def __repr__(self) -> str:  # Just representation
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"


# Post - One to Many Relationship
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)

    user: Mapped[list["User"]] = relationship(
        "User",
        back_populates="posts",
    )

    def __repr__(self) -> str:  # Just representation
        return f"<Posts(id={self.id}, title={self.title})>"


# Post - One to One Relationship
class Profile(Base):
    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True
    )
    bio: Mapped[str] = mapped_column(String, nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="profile")

    def __repr__(self) -> str:  # Just representation
        return f"<Profile(id={self.id}, user_id={self.user_id})>"


# Address - Many to Many Relationship
class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True
    )
    street: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # String length is 50
    country: Mapped[str] = mapped_column(String, nullable=False)
    user: Mapped[list["User"]] = relationship("User", back_populates="address")

    def __repr__(self) -> str:  # Just representation
        return f"<Address id={self.id}, street={self.street} country={self.country}>"


# Address association table / junction table
user_address_association = Table(
    "user_address_association",
    Base.metadata,
    Column(
        "user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "address_id",
        Integer,
        ForeignKey("address.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)

# -----------------------------------
# Don't require due to Alembic
# Create Table
# def create_tables():
#     Base.metadata.create_all(engine)


# Drop Table
# def drop_tables():
#     Base.metadata.drop_all(engine)
