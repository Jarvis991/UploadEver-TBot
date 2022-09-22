#Copyright 2022-present, Author: 5MysterySD

import os
import logging
from time import time
from logging.handlers import RotatingFileHandler

# Logging >>>
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %I:%M:%S %p",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=50000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

# Initial >>>
USERS_API = {}
BOT_UPTIME = time()

# Invoke Data >>>
class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DIRECTORY = os.environ.get("DIRECTORY", "downloads/")
    ADMINS = list(set(int(x) for x in os.environ.get("ADMINS", "0").split()))
    MONGODB_URI = os.environ.get("DATABASE_URL", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100"))
