from tables import create_table, drop_table
import asyncio


async def main():
    await create_table()


if __name__ == "__main__":
    asyncio.run(main())
