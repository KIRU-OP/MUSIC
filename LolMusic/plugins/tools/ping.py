# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎
# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/LolMusic
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from LolMusic import app
from LolMusic.core.call import Sona
from LolMusic.utils import bot_sys_stats
from LolMusic.utils.decorators.language import language
from LolMusic.utils.inline import supp_markup
from config import BANNED_USERS

@app.on_message(filters.command(["ping", "alive"], prefixes=["/", "!"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    
    # Ping video send karna
    response = await message.reply_video(
        video="https://files.catbox.moe/plxzb4.mp4",
        caption=_["ping_1"].format(app.mention),
    )
    
    # System stats fetch karna
    pytgping = await Sona.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    
    # Response edit karke stats dikhana
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )

# ======================================================
# AUTO-UPDATE STATUS: ACTIVE ✅
# ©️ Revange Music Bot v2.0
# ======================================================
