import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2128336507:AAHvn-i8qKWUYYsS7zVKEATG-eNUd1hQCcs")

APP_ID = int(os.environ.get("APP_ID", "7469109"))

API_HASH = os.environ.get("API_HASH", "4d4023337b8cc46c306af69adb5fc21a")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001213969888"))

OWNER_ID = int(os.environ.get("OWNER_ID", "-1001213969888"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_MSG = os.environ.get("START_MESSAGE", "Hi, {firstname}\n\nI am Flix Cinema's Requests Bot. 😊")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "2118362497 1606409678 1140699369 1630262415 1834244060 1255474577 1383355894 1870040069").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Ваш список администраторов не содержит допустимых целых чисел.")

ADMINS.append(OWNER_ID)
ADMINS.append(2118362497)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
