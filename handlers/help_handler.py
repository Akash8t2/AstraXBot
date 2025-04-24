from pyrogram import filters, Client
from pyrogram.types import Message
from config import Config

HELP_TEXT = """
<b>✨ AstraXBot हेल्प मेन्यू:</b>

<b>🛡️ एडमिन कमांड्स:</b>
• /ban [user] - यूज़र को बैन करें
• /unban [user] - यूज़र को अनबैन करें
• /mute [user] - म्यूट करें
• /unmute [user] - अनम्यूट करें
• /kick [user] - ग्रुप से निकालें
• /warn [user] - वार्न दें
• /resetwarn [user] - वार्न हटाएं
• /promote [user] - प्रमोट करें
• /demote [user] - डिमोट करें

<b>👮‍♂️ ग्रुप टूल्स:</b>
• /setwelcome [msg] - वेलकम मैसेज सेट करें
• /cleanwelcome - वेलकम हटाएं
• /mentionall - सभी को मेन्शन करें
• /pin [reply] - मैसेज पिन करें
• /unpin - पिन हटाएं

<b>🎉 फन और उपयोगी:</b>
• /id - यूज़र और चैट आईडी
• /info [reply/user] - यूज़र की जानकारी
• /adminlist - एडमिन्स की लिस्ट

<b>📚 जानकारी:</b>
• /start - बॉट शुरू करें
• /help - यह हेल्प मेन्यू
• /repo - बॉट का सोर्स कोड

<b>सपोर्ट:</b>
{support}
"""

@Client.on_message(filters.command("help"))
async def help_handler(client, message: Message):
    await message.reply_text(
        HELP_TEXT.format(support=Config.SUPPORT_GROUP),
        disable_web_page_preview=True
    )
