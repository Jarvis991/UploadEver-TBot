import asyncio
from bot import bot
from bot.core.db.db_func import db

if __name__ == "__main__":
    asyncio.run(db.db_load())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    bot.run()
