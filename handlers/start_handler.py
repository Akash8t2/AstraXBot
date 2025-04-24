from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ChatType
from config import Config
from pyrogram import Client

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    await message.reply_text(
        f"नमस्ते {message.from_user.first_name}!\n\n"
        f"मैं AstraXBot हूँ - एक पावरफुल टेलीग्राम ग्रुप मैनेजमेंट बॉट।\n"
        f"मुझे अपने ग्रुप में जोड़कर पूरा कंट्रोल पाएं।\n\n"
        f"मदद के लिए /help कमांड का उपयोग करें।\n"
        f"सपोर्ट ग्रुप: {Config.SUPPORT_GROUP}\n"
        f"अपडेट्स: {Config.UPDATE_CHANNEL}"
    )

@Client.on_message(filters.command("start") & filters.group)
async def start_in_group(client, message: Message):
    await message.reply_text("बॉट एक्टिव है इस ग्रुप में। /help टाइप करें ज़्यादा जानकारी के लिए।")
