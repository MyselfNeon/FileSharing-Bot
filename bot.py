from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
import sys
from datetime import datetime
from pytz import timezone
from config import (
    API_HASH, API_ID, BOT_TOKEN, TG_BOT_WORKERS,
    FORCE_SUB_CHANNEL, CHANNEL_ID, PORT, LOG_CHANNEL
)
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009999999999


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={"root": "plugins"},
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
        ist = timezone("Asia/Kolkata")
        now = datetime.now(ist)
        restart_text = (
            f"✅ <b>{bot_name} Bot Is Restarted</b>\n\n"
            f"📅 <b>Date :</b> {now.strftime('%d-%b-%Y')}\n"
            f"⏰ <b>Time :</b> {now.strftime('%I:%M %p')}\n"
            f"🌐 <b>Timezone :</b> Asia/Kolkata\n"
            f"🉐 <b>Version :</b> Pyrogram {pyrogram.__version__}"
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
        f"#𝖭𝖾𝗐𝖴𝗌𝖾𝗋 𝖲𝗍𝖺𝗋𝗍𝖾𝖽 𝖳𝗁𝖾 𝖡𝗈𝗍\n\n"
        f"🆔 <b>User ID :</b> <code>{user.id}</code>\n"
        f"👤 <b>Username :</b> @{user.username if user.username else 'None'}\n"
        f"🔗 <b>User Link :</b> {user.mention}"
    )
    await client.send_message(LOG_CHANNEL, log_text)
    await message.reply_text("👋 Hello! You started the bot ✅")
