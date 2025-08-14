from models import create_tables
from services import *
import asyncio


async def main():
    # await create_tables()

    # Create user
    result = await create_user("mahipal", "hello@gmail.com")
    print("user created: ", result)


if __name__ == "__main__":
    asyncio.run(main())
