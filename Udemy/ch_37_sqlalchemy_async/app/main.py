from tables import create_table, drop_table
import asyncio
from services import *


async def main():
    # await create_table()

    # Create table
    # await create_user("mahipal", "hello@gmail.com")

    # Get all users
    result = await get_all_users()
    print("Result: ", result)


if __name__ == "__main__":
    asyncio.run(main())
