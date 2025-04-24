import os
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from handlers import start_handler, help_handler, ban_handler, unban_handler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Pyrogram Client
app = Client("AstraXBot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

# Command Handlers
app.add_handler(start_handler)
app.add_handler(help_handler)
app.add_handler(ban_handler)
app.add_handler(unban_handler)

# Other Handlers and Filters can be added here

if __name__ == "__main__":
    app.run()
