# handlers/help_handler.py

from pyrogram import Client, filters
from pyrogram.types import Message

HELP_TEXT = """
**AstraXBot Commands:**

**General:**
/start - बॉट शुरू करें
/help - सभी कमांड्स देखें
/id - अपना या रिप्लाई किए गए यूजर का आईडी लें

**Group Management:**
/promote - यूजर को एडमिन बनाएँ (रिप्लाई में)
/demote - एडमिन हटाएँ
/pin - मैसेज पिन करें (रिप्लाई में)
/unpin - पिन हटाएँ
/mute - यूजर को म्यूट करें
/unmute - म्यूट हटाएँ
/ban - यूजर को बैन करें
/unban - बैन हटाएँ
/warn - वार्न दें
/warnings - वार्निंग्स देखें
/resetwarns - वार्निंग्स रीसेट करें

**Utilities:**
/setwelcome - वेलकम मैसेज सेट करें
/getwelcome - वेलकम मैसेज देखें
/delwelcome - वेलकम मैसेज हटाएँ
/mentionall - सभी को टैग करें

**Fun & Extra:**
/repo - GitHub लिंक
/stats - बॉट की स्थिति

Support: @BeatXFlowSupport  
Updates: @BeatFlowCommunity
"""

@Client.on_message(filters.command("help") & filters.private)
async def help_private(client, message: Message):
    await message.reply_text(HELP_TEXT, disable_web_page_preview=True)

@Client.on_message(filters.command("help") & filters.group)
async def help_group(client, message: Message):
    await message.reply_text("**Help के लिए मुझे प्राइवेट में यूज़ करें।**\n/start दबाएँ: @botcasx", quote=True)
