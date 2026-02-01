# ======================================================
# ©️ 2025-26 ᴘʀᴇᴍɪᴜᴍ ᴄᴏᴅᴇ ʙʏ ʀᴇᴠᴀɴɢᴇ 😎
# 🧑‍💻 Developer : t.me/dmcatelegram
# 📢 Channel : t.me/dmcatelegram
# 🛠 Version : 4.0 (Modern UI)
# ======================================================

import time
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from LolMusic import app
import config
from LolMusic.utils.formatters import get_readable_time

# ======================================================
# UPTIME
# ======================================================
START_TIME = time.time()

# ======================================================
# MODERN TEXT (NO OLD STYLE)
# ======================================================

REPO_TEXT = """
👋 **Hey {name}**

Welcome to **Kiru Tech**  
A modern hub for our public music & utility bots.

• Status : 🟢 Online  
• Version : v4.0  
• Uptime : `{uptime}`  

Some repositories are kept **private** for security reasons.  
You can freely use our **public bots** below 👇
"""

# ======================================================
# /repo COMMAND
# ======================================================

@app.on_message(filters.command("repo"))
async def repo_command(_, message: Message):

    uptime = get_readable_time(int(time.time() - START_TIME))

    buttons = [
        [
            InlineKeyboardButton("🎧 Aaru Music", url="https://t.me/aaru_music_rbot"),
            InlineKeyboardButton("🎶 Nikku Muzic", url="https://t.me/NIKKU_ROBOT"),
        ],
        [
            InlineKeyboardButton("🎵 Radha Music", url="https://t.me/RADHAVIBEBOT"),
            InlineKeyboardButton("🎼 Shyam Music", url="https://t.me/SHYAMVIBEBOT"),
        ],
        [
            InlineKeyboardButton("💬 Support", url="https://t.me/NOBITA_SUPPORT"),
            InlineKeyboardButton("📢 Channel", url="https://t.me/VnioxTechApi"),
        ],
        [
            InlineKeyboardButton("👨‍💻 Developer", user_id=config.OWNER_ID),
        ],
        [
            InlineKeyboardButton(
                "➕ Add me to your group",
                url=f"https://t.me/{app.username}?startgroup=true"
            )
        ]
    ]

    await message.reply_photo(
        photo="https://graph.org/file/46a60562ff98cc1180237-0b722292cd1bcca02f.jpg",
        caption=REPO_TEXT.format(
            name=message.from_user.first_name,
            uptime=uptime
        ),
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# ======================================================
# Powered by @dmcatelegram
# ======================================================
