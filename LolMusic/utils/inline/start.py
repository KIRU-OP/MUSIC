gh# ======================================================
# ©️ 2025-26 ᴘʀᴇᴍɪᴜᴍ ᴄᴏᴅᴇ ʙʏ ʀᴇᴠᴀɴɢᴇ 😎
# 🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : t.me/dmcatelegram
# 📢 ᴄʜᴀɴɴᴇʟ : t.me/dmcatelegram
# 🛠 ᴍᴏᴅɪғɪᴇᴅ ᴘᴀɴᴇʟs ᴠᴇʀsɪᴏɴ
# =======================================================

from pyrogram.types import InlineKeyboardButton
import config
from LolMusic import app

def start_panel(_):
    """
    Buttons shown when the bot is in a Group
    """
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ " + _["S_B_1"], 
                url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(
                text="💬 sᴜᴘᴘᴏʀᴛ", 
                url=config.SUPPORT_CHAT
            ),
        ],
        [
            InlineKeyboardButton(
                text="📢 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", 
                url="https://t.me/dmcatelegram"
            )
        ]
    ]
    return buttons


def private_panel(_):
    """
    Buttons shown when the bot is in Private DM
    """
    buttons = [
        [
            InlineKeyboardButton(
                text="✨ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✨",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="📖 ᴄᴏᴍᴍᴀɴᴅs", 
                callback_data="MAIN_CP"
            ),
            InlineKeyboardButton(
                text="⚙️ sᴜᴘᴘᴏʀᴛ", 
                url=config.SUPPORT_CHAT
            ),
        ],
        [
            InlineKeyboardButton(
                text="👑 ᴏᴡɴᴇʀ", 
                user_id=config.OWNER_ID
            ),
            InlineKeyboardButton(
                text="ℹ️ ᴀʙᴏυᴛ", 
                callback_data="ALLBOT_CP"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🚀 ᴍᴏʀᴇ ᴘʀᴏᴊᴇᴄᴛs", 
                url="https://t.me/KIRU_OP"
            )
        ],
    ]
    return buttons

# ======================================================
# ⚡ ᴜᴘɢʀᴀᴅᴇᴅ ʙʏ : @dmcatelegram
# ======================================================
