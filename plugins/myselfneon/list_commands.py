# plugins/global_commands_logger.py

from pyrogram import Client
from pyrogram.types import BotCommand
from info import LOG_CHANNEL  # Import from your info.py

# 🔹 Your commands
COMMANDS = [
    ("/start", "Start the bot"),
    ("/help", "Show help message"),
    ("/id", "Get your user ID"),
    ("/about", "About this bot"),
]

@Client.on_start
async def set_global_commands_with_log(client: Client):
    try:
        # Convert simple list to BotCommand objects
        new_commands = [BotCommand(cmd, desc) for cmd, desc in COMMANDS]
        
        # Get current commands
        old_commands = await client.get_bot_commands()
        old_set = set((c.command, c.description) for c in old_commands)
        new_set = set((c.command, c.description) for c in new_commands)

        # Determine changes
        added = new_set - old_set
        removed = old_set - new_set

        # Update commands globally
        await client.set_bot_commands(new_commands)

        # Prepare log message
        log_text = "**🤖 Bot Commands Updated**\n\n"
        if added:
            log_text += "**➕ Added Commands:**\n" + "\n".join([f"{c[0]} - {c[1]}" for c in added]) + "\n\n"
        if removed:
            log_text += "**➖ Removed Commands:**\n" + "\n".join([f"{c[0]} - {c[1]}" for c in removed]) + "\n\n"
        if not added and not removed:
            log_text += "No changes detected. ✅"

        # Send log to channel from info.py
        await client.send_message(LOG_CHANNEL, log_text)

        print("✅ Global commands updated successfully.")
    except Exception as e:
        print(f"❌ Failed to set global commands: {e}")
