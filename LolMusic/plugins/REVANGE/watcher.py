# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/LolMusic
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from pyrogram import filters
from pyrogram.types import Message

from LolMusic import app
from LolMusic.core.call import Sona

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Sona.stop_stream_force(message.chat.id)

# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/LolMusic
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================
