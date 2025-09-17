import os

# ------------------ Bot Settings ------------------ #
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
OWNER_ID = int(os.environ.get("OWNER_ID", "841851780"))

# ------------------ Database ------------------ #
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "MyselfNeon")

# ------------------ Channels ------------------ #
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001889915480"))
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002487845241"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002384933640"))

# ------------------ Bot Config ------------------ #
FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "300"))
PORT = int(os.environ.get("PORT", "8080"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# ------------------ Admins ------------------ #
ADMINS = [OWNER_ID, 841851780] + [int(x) for x in os.environ.get("ADMINS", "").split() if x.isdigit()]

# ------------------ Bot Messages ------------------ #
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION")
PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "False") == "True"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == "True"

START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b><i>Hᴇʟʟᴏ {mention} ✨\n\n"
    "I ᴀᴍ Pᴇʀᴍᴀɴᴇɴᴛ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ.\n"
    "Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ <a href='https://t.me/MyselfNeon'>NᴇᴏɴAɴᴜʀᴀɢ</a>.\n\n"
    "Gᴇᴛ Rᴇᴅɪʀᴇᴄᴛᴇᴅ Fʀᴏᴍ Cᴏʀʀᴇᴄᴛ Lɪɴᴋs Tᴏ Gᴇᴛ Tʜᴇ Fɪʟᴇs 🖇️</i></b>"
)

FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b><i>Hᴇʟʟᴏ {mention}\n\n"
    "Yᴏᴜ Nᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ Mʏ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ ᴛᴏ Usᴇ Mᴇ\n\n</i></b>"
)

BOT_STATS_TEXT = "<b><i>Bᴏᴛ Uᴘᴛɪᴍᴇ</i> :</b>\n{uptime}"


# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
