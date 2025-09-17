from pyrogram import __version__
from bot import Bot  # no need to import bot_name anymore
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data

    if data == "about":
        # Use client.username dynamically
        bot_username = client.username or "NeonFilesBot"

        await query.message.edit_text(
            text=(
                f"<b>🤖 <i>Mʏ Nᴀᴍᴇ :</i></b> "
                f"<a href='https://t.me/{bot_username}'><b><i>{bot_username}</i></b></a>\n"
                f"<b>📝 <i>Lᴀɴɢᴜᴀɢᴇ :</i></b> "
                f"<a href='https://python.org'><b><i>Pʏᴛʜᴏɴ 3</i></b></a>\n"
                f"<b>📚 <i>Lɪʙʀᴀʀʏ :</i></b> "
                f"<a href='https://pyrogram.org'><b><i>Pʏʀᴏɢʀᴀᴍ {__version__}</i></b></a>\n"
                f"<b>🚀 <i>Sᴇʀᴠᴇʀ :</i></b> "
                f"<a href='https://heroku.com'><b><i>Hᴇʀᴏᴋᴜ</i></b></a>\n"
                f"<b>📢 <i>Cʜᴀɴɴᴇʟ :</i></b> "
                f"<a href='https://t.me/NeonFiles'><b><i>NᴇᴏɴFɪʟᴇs</i></b></a>\n"
                f"<b>🧑‍💻 <i>Dᴇᴠᴇʟᴏᴘᴇʀ :</i></b> "
                f"<a href='tg://user?id={OWNER_ID}'><b><i>NᴇᴏɴAɴᴜʀᴀɢ</i></b></a>"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data="close")]
                ]
            ),
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
