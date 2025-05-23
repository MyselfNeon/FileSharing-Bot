import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")


OWNER_ID = int(os.environ.get("OWNER_ID", "841851780"))
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "MyselfNeon")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002487845241"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002384933640"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "300")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6848088376]
    for x in (os.environ.get("ADMINS", "841851780").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "<b><i>Please don't Send Me Messages Directly I am just File Sharing Bot 😄</i></b>"

START_MSG = os.environ.get("START_MESSAGE", "<b><i>Hello {mention}\n\nI am Permanent File Store Bot.\nDeveloped by <a href='https://t.me/MyselfNeon'>NeonAnurag</a>.\n\nGet Redirected from Correct Links to get the Files 🖇️</i></b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b><i>Hello {mention}\n\nYou Need To Join In My Channel/Group To Use Me\n\n</i></b>")





ADMINS.append(OWNER_ID)
ADMINS.append(841851780)

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
   





# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
