from bot import bot
from bot.core.db.db_func import db

if __name__ == "__main__":

    db.db_load()
    bot.run()
