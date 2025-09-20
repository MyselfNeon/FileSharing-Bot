# Bot.py
import os
from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, BotCommand
import sys
from datetime import datetime, timedelta, timezone
from config import (
    API_HASH, API_ID, BOT_TOKEN, TG_BOT_WORKERS,
    FORCE_SUB_CHANNEL, CHANNEL_ID, PORT, LOG_CHANNEL
)
import pyrogram.utils
import pyrogram  # ✅ For version info

pyrogram.utils.MIN_CHANNEL_ID = -1009999999999

IST = timezone(timedelta(hours=5, minutes=30))

def get_all_plugins(path="plugins"):
    """
    Recursively find all .py files in the plugins folder (excluding __init__.py and this loader)
    and return a dict suitable for Client(plugins=...)
    """
    plugins_dict = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                # get relative path from plugins folder
                rel_path = os.path.relpath(os.path.join(root, file), path)
                # convert path to module notation for Pyrogram
                module_path = rel_path.replace(os.sep, ".")[:-3]  # remove .py
                plugins_dict[module_path] = {}
    return plugins_dict

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={"root": "plugins", **get_all_plugins("plugins")},  # ✅ Auto-load all plugins
            workers=TG_BOT_WORKERS,
            bot_token=BOT_TOKEN
        )

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        self.username = usr_bot_me.username
        bot_name = usr_bot_me.first_name

        # Force Sub Check
        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                await self.send_message(
                    LOG_CHANNEL,
                    f"❌ Failed to get invite link for FORCE_SUB_CHANNEL\n\nError: `{a}`"
                )
                sys.exit()

        # DB Channel Check
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
        except Exception as e:
            await self.send_message(
                LOG_CHANNEL,
                f"❌ Failed to connect DB channel.\nError: `{e}`\n\nCheck CHANNEL_ID: `{CHANNEL_ID}`"
            )
            sys.exit()

        # Bot Restart Log
        now = datetime.now(IST)
        restart_text = (
            f"**♻️ __{bot_name} Bot Restarted__**\n\n"
            f"**📅 __Date :__** __{now.strftime('%d-%b-%Y')}__\n"
            f"**⏰ __Time :__** __{now.strftime('%I:%M %p')}__\n"
            f"**🌐 __Timezone :__** __Asia/Kolkata            __\n"
            f"**🉐 __Version :__** __Pyrogram {pyrogram.__version__}__"
        )
        await self.send_message(LOG_CHANNEL, restart_text)

        self.set_parse_mode(ParseMode.HTML)

        # Web response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        await self.send_message(LOG_CHANNEL, "❌ Bot Stopped!")

# 🔹 Log New Users
@Bot.on_message(filters.command("start") & filters.private)
async def log_new_user(client: Bot, message: Message):
    user = message.from_user
    log_text = (
        f"**#𝖭𝖾𝗐𝖴𝗌𝖾𝗋 👤**\n\n"
        f"**__@NeonFilesBot__**\n\n"
        f"**🆔 __User ID :__** <code>{user.id}</code>\n"
        f"**👤 __Username :__** __@{user.username if user.username else 'None'}__\n"
        f"**🖇️ __User Link :__** __{user.mention}__"
    )
    await client.send_message(LOG_CHANNEL, log_text)
    await message.reply_text("👋 Hello! You started the bot ✅")
