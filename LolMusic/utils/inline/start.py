# ⚡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⚡
# 🛠️ PROJECT  : LolMusic Framework v3.0 [PRO]
# 🛡️ LICENSE  : © 2025-2030 Revange Ecosystem
# 🚀 STATUS   : Future-Ready | Optimized
#
# 🧑‍💻 DEVELOPER: t.me/dmcatelegram
# 📢 CHANNEL  : t.me/dmcatelegram
# 🔗 SOURCE   : https://github.com/hexamusic/LolMusic
# ⚡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⚡

from pyrogram.types import InlineKeyboardButton
import config
from LolMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton("✨ ᴀʙᴏᴜᴛ", callback_data="ALLBOT_CP"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="MAIN_CP"),
        ],
    ]
    return buttons

# 🛸━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🛸
# ⚡ BUILT FOR PERFORMANCE | REVANGE 🔥
# 📅 LAST UPDATE: JANUARY 2025 (Next-Gen Version)
# 🛸━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🛸
