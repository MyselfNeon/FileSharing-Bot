from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import API_HASH, API_ID, LOGGER, BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, PORT
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
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bᴏᴛ Cᴀɴ'ᴛ Exᴘᴏʀᴛ Iɴᴠɪᴛᴇ Lɪɴᴋ Fʀᴏᴍ Fᴏʀᴄᴇ Sᴜʙ Cʜᴀɴɴᴇʟ!")
                self.LOGGER(__name__).warning(f"Pʟᴇᴀsᴇ Dᴏᴜʙʟᴇ Cʜᴇᴄᴋ Tʜᴇ FORCE_SUB_CHANNEL Vᴀʟᴜᴇ Aɴᴅ Mᴀᴋᴇ Sᴜʀᴇ Bᴏᴛ ɪs Aᴅᴍɪɴ ɪɴ Cʜᴀɴɴᴇʟ Wɪᴛʜ Iɴᴠɪᴛᴇ Usᴇʀs Vɪᴀ Lɪɴᴋ Pᴇʀᴍɪssɪᴏɴ, Cᴜʀʀᴇɴᴛ Fᴏʀᴄᴇ Sᴜʙ Cʜᴀɴɴᴇʟ Vᴀʟᴜᴇ: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBᴏᴛ Sᴛᴏᴘᴘᴇᴅ. https://t.me/MyselfNeon Fᴏʀ Sᴜᴘᴘᴏʀᴛ")
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "**__NᴇᴏɴFɪʟᴇsBᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ ... 👨‍💻♻️__** \n**__Cʀᴇᴀᴛᴇᴅ ʙʏ Aɴᴜʀᴀɢ-Aɴsʜɪᴋᴀ ❤️...__**")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Mᴀᴋᴇ Sᴜʀᴇ Bᴏᴛ ɪs Aᴅᴍɪɴ ɪɴ DB Cʜᴀɴɴᴇʟ, Aɴᴅ Dᴏᴜʙʟᴇ Cʜᴇᴄᴋ Tʜᴇ CHANNEL_ID Vᴀʟᴜᴇ, Cᴜʀʀᴇɴᴛ Vᴀʟᴜᴇ: {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBᴏᴛ Sᴛᴏᴘᴘᴇᴅ. Jᴏɪɴ https://t.me/NeonFiles Fᴏʀ Sᴜᴘᴘᴏʀᴛ")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bᴏᴛ Rᴜɴɴɪɴɢ...!\n\nCʀᴇᴀᴛᴇᴅ Bʏ \nhttps://t.me/NeonFiles")
        self.LOGGER(__name__).info(f"""ミ💖✨ NEONFILES ✨💖彡""")
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bᴏᴛ Sᴛᴏᴘᴘᴇᴅ...❌")
            





# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
