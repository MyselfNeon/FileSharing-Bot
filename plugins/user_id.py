from pyrogram import filters, enums
from pyrogram.types import Message
from bot import Bot


@Bot.on_message(filters.command("id", prefixes=["/"]))
async def showid(client, message: Message):
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        user_id = message.from_user.id
        await message.reply_text(
            f"<b>__Your User ID Is__ :</b> <code>{user_id}</code>",
            quote=True
        )
    else:
        chat_id = message.chat.id
        await message.reply_text(
            f"<b>__This Chat ID Is__ :</b> <code>{chat_id}</code>",
            quote=True
        )
        


# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
