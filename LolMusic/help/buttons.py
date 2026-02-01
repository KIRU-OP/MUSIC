# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎
# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/LolMusic
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from LolMusic import app

class BUTTONS(object):
    # BBUTTON: Compact style with 3 buttons per row + Emojis
    BBUTTON = [
        [
            InlineKeyboardButton("⚡ ᴀᴄᴛɪᴏɴ", callback_data="TOOL_BACK HELP_06"),
            InlineKeyboardButton("🛡️ ғʟᴏᴏᴅ", callback_data="TOOL_BACK HELP_11"),
            InlineKeyboardButton("✅ ᴀᴘᴘʀᴏᴠᴇ", callback_data="TOOL_BACK HELP_12"),
        ],
        [
            InlineKeyboardButton("🤖 ɢᴘᴛ", callback_data="TOOL_BACK HELP_01"),
            InlineKeyboardButton("📂 ɢɪᴛʜᴜʙ", callback_data="TOOL_BACK HELP_09"),
            InlineKeyboardButton("👥 ɢʀᴏᴜᴘ", callback_data="TOOL_BACK HELP_07"),
        ],
        [
            InlineKeyboardButton("📜 ʜɪsᴛᴏʀʏ", callback_data="TOOL_BACK HELP_08"),
            InlineKeyboardButton("ℹ️ ɪɴғᴏ", callback_data="TOOL_BACK HELP_03"),
            InlineKeyboardButton("🧹 ᴘᴜʀɢᴇ", callback_data="TOOL_BACK HELP_13"),
        ],
        [
            InlineKeyboardButton("🎨 sᴛɪᴄᴋᴇʀ", callback_data="TOOL_BACK HELP_05"),
            InlineKeyboardButton("📣 ᴛᴀɢ-ᴀʟʟ", callback_data="TOOL_BACK HELP_04"),
            InlineKeyboardButton("🛠️ ᴛᴏᴏʟs", callback_data="TOOL_BACK HELP_10"),
        ],
        [
            InlineKeyboardButton("🎙️ ᴠᴄ-ᴛᴏᴏʟ", callback_data="TOOL_BACK HELP_14"),
            InlineKeyboardButton("🤫 ᴡʜɪsᴘᴇʀ", callback_data="TOOL_BACK HELP_02"),
            InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="MAIN_CP"),
        ]
    ]
    
    # PBUTTON: Contact info
    PBUTTON = [
        [
            InlineKeyboardButton("📩 ᴄᴏɴᴛᴀᴄᴛ", url="https://t.me/dmcatelegram"),
            InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="MAIN_CP"),
        ]
    ]
    
    # ABUTTON: Support & Privacy
    ABUTTON = [
        [
            InlineKeyboardButton("🆘 sᴜᴘᴘᴏʀᴛ", url="https://t.me/dmcatelegram"),
            InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/dmcatelegram"),
            InlineKeyboardButton("🔐 ᴘʀɪᴠᴀᴄʏ", url="https://telegra.ph/Privacy-Policy--REVANG-08-06"),
        ],
        [  
            InlineKeyboardButton("🔙 ʙᴀᴄᴋ ᴛᴏ sᴇᴛᴛɪɴɢs", callback_data="settingsback_helper"),
        ]
    ]
    
    # SBUTTON: Main Settings
    SBUTTON = [
        [
            InlineKeyboardButton("🎵 ᴍᴜsɪᴄ", callback_data="settings_back_helper"),
            InlineKeyboardButton("⚙️ ᴍᴀɴᴀɢᴇ", callback_data="TOOL_CP"),
        ],
        [
            InlineKeyboardButton("🏠 ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="settingsback_helper"),
        ]
    ]

# ======================================================
# UI Refined by Revange 😎
# ======================================================
