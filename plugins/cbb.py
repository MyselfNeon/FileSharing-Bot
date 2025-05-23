from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🤖 <i>Mʏ Nᴀᴍᴇ :</i></b> <a href='https://t.me/NeonFilesBot'><b><i>NᴇᴏɴFɪʟᴇsBᴏᴛ</i></b></a> \n<b>📝 <i>Lᴀɴɢᴜᴀɢᴇ :</i></b> <a href='https://python.org'><b><i>Pʏᴛʜᴏɴ 3</i></b></a> \n<b>📚 <i>Lɪʙʀᴀʀʏ :</i></b> <a href='https://pyrogram.org'><b><i>Pʏʀᴏɢʀᴀᴍ {__version__}</i></b></a> \n<b>🚀 <i>Sᴇʀᴠᴇʀ :</i></b> <a href='https://heroku.com'><b><i>Hᴇʀᴏᴋᴜ</i></b></a> \n<b>📢 <i>Cʜᴀɴɴᴇʟ :</i></b> <a href='https://t.me/NeonFiles'><b><i>NᴇᴏɴFɪʟᴇs</i></b></a> \n<b>🧑‍💻 <i>Dᴇᴠᴇʟᴏᴘᴇʀ :</i></b> <a href='tg://user?id={OWNER_ID}'><b><i>NᴇᴏɴAɴᴜʀᴀɢ</i></b></a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
