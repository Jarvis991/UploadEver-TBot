#Copyright 2022-present, Author: 5MysterySD

from os import environ as env
import logging
from logging import StreamHandler, basicConfig, INFO
from time import time
from logging.handlers import RotatingFileHandler

# Logging >>>
basicConfig(
    level=INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %I:%M:%S %p",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=50000000, backupCount=10
        ),
        StreamHandler(),
    ],
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

# Initial >>>
BOT_UPTIME = time()

# Invoke Data >>>
class Config:
    API_ID = int(env.get("API_ID", ""))
    API_HASH = env.get("API_HASH", "")
    BOT_TOKEN = env.get("BOT_TOKEN", "")
    DIRECTORY = env.get("DIRECTORY", "downloads/")
    ADMINS = list(set(int(x) for x in env.get("ADMINS", "0").split()))
    MONGODB_URI = env.get("DATABASE_URL", "")
    LOG_CHANNEL = int(env.get("LOG_CHANNEL", "-100"))
