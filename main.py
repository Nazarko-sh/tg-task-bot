import asyncio

from app.bot import create_bot, create_dispatcher
from app.db import init_db

async def main():
    await init_db()
    bot = create_bot()
    dp = create_dispatcher()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
