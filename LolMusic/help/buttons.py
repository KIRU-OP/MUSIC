# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎
# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/LolMusic
# 📢 Telegram channel : t.me/dmcatelegram
# ======================================================

from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)

from LolMusic import app   # LolMusic main client

# ======================================================
# BUTTONS
# ======================================================

class BUTTONS(object):

    BBUTTON = [
        [
            InlineKeyboardButton("ᴀᴄᴛɪᴏɴ", callback_data="HELP_06"),
            InlineKeyboardButton("ᴀɴᴛɪ ғʟᴏᴏᴅ", callback_data="HELP_11"),
            InlineKeyboardButton("ᴀᴘᴘʀᴏᴠᴀʟ", callback_data="HELP_12"),
        ],
        [
            InlineKeyboardButton("ᴄʜᴀᴛɢᴘᴛ", callback_data="HELP_01"),
            InlineKeyboardButton("ɢɪᴛʜᴜʙ", callback_data="HELP_09"),
            InlineKeyboardButton("ɢʀᴏᴜᴘ", callback_data="HELP_07"),
        ],
        [
            InlineKeyboardButton("ʜɪsᴛᴏʀʏ", callback_data="HELP_08"),
            InlineKeyboardButton("ɪɴғᴏ", callback_data="HELP_03"),
            InlineKeyboardButton("ᴘᴜʀɢᴇ", callback_data="HELP_13"),
        ],
        [
            InlineKeyboardButton("sᴛɪᴄᴋᴇʀ", callback_data="HELP_05"),
            InlineKeyboardButton("ᴛᴀɢ ᴀʟʟ", callback_data="HELP_04"),
            InlineKeyboardButton("ᴛᴏᴏʟs", callback_data="HELP_10"),
        ],
        [
            InlineKeyboardButton("ᴠᴄ ᴛᴏᴏʟs", callback_data="HELP_14"),
            InlineKeyboardButton("ᴡʜɪsᴘᴇʀ", callback_data="HELP_02"),
        ],
        [
            InlineKeyboardButton("ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="HELP_HOME"),
        ]
    ]


# ======================================================
# /help COMMAND
# ======================================================

@app.on_message(filters.command("help"))
async def help_cmd(_, message: Message):
    await message.reply_text(
        text=(
            "✨ **ʜєʟᴘ ᴍᴇɴᴜ** ✨\n\n"
            "ɴɪᴄʜᴇ ᴅɪʏᴇ ɢᴀʏᴇ ʙᴜᴛᴛᴏɴs sᴇ\n"
            "ᴀᴘɴᴇ ʙᴏᴛ ᴋᴇ ғᴇᴀᴛᴜʀᴇs ᴅᴇᴋʜᴇɴ 🚀"
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS.BBUTTON)
    )


# ======================================================
# CALLBACK HANDLERS
# ======================================================

@app.on_callback_query(filters.regex("^HELP_"))
async def help_callbacks(_, query: CallbackQuery):

    data = query.data

    if data == "HELP_HOME":
        await query.message.edit_text(
            "✨ **ʜєʟᴘ ᴍᴇɴᴜ** ✨",
            reply_markup=InlineKeyboardMarkup(BUTTONS.BBUTTON)
        )
        return

    help_texts = {
        "HELP_01": "🤖 **ᴄʜᴀᴛɢᴘᴛ**\n\nᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ & ǫᴜᴇsᴛɪᴏɴs.",
        "HELP_02": "💬 **ᴡʜɪsᴘᴇʀ**\n\nsᴇᴄʀᴇᴛ ᴍᴇssᴀɢᴇ ғᴇᴀᴛᴜʀᴇ.",
        "HELP_03": "ℹ️ **ɪɴғᴏ**\n\nᴜsᴇʀ & ɢʀᴏᴜᴘ ɪɴғᴏ.",
        "HELP_04": "🏷 **ᴛᴀɢ ᴀʟʟ**\n\nᴀʟʟ ᴍᴇᴍʙᴇʀs ᴍᴇɴᴛɪᴏɴ.",
        "HELP_05": "🖼 **sᴛɪᴄᴋᴇʀ**\n\nsᴛɪᴄᴋᴇʀ ᴛᴏᴏʟs.",
        "HELP_06": "⚙️ **ᴀᴄᴛɪᴏɴ**\n\nᴀᴅᴍɪɴ ᴀᴄᴛɪᴏɴs.",
        "HELP_07": "👥 **ɢʀᴏᴜᴘ**\n\nɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ.",
        "HELP_08": "🕘 **ʜɪsᴛᴏʀʏ**\n\nᴘʀᴇᴠɪᴏᴜs ᴀᴄᴛɪᴠɪᴛʏ.",
        "HELP_09": "🌐 **ɢɪᴛʜᴜʙ**\n\nɢɪᴛʜᴜʙ ɪɴᴛᴇɢʀᴀᴛɪᴏɴ.",
        "HELP_10": "🛠 **ᴛᴏᴏʟs**\n\nᴇxᴛʀᴀ ᴜᴛɪʟɪᴛɪᴇs.",
        "HELP_11": "🛡 **ᴀɴᴛɪ ғʟᴏᴏᴅ**\n\nsᴘᴀᴍ ᴄᴏɴᴛʀᴏʟ.",
        "HELP_12": "📌 **ᴀᴘᴘʀᴏᴠᴀʟ**\n\nɴᴇᴡ ᴜsᴇʀ ᴀᴘᴘʀᴏᴠᴀʟ.",
        "HELP_13": "🧹 **ᴘᴜʀɢᴇ**\n\nᴍᴇssᴀɢᴇ ᴅᴇʟᴇᴛᴇ.",
        "HELP_14": "🎧 **ᴠᴄ ᴛᴏᴏʟs**\n\nᴠᴏɪᴄᴇ ᴄʜᴀᴛ ғᴇᴀᴛᴜʀᴇs.",
    }

    text = help_texts.get(data, "❌ ɴᴏ ɪɴғᴏ.")

    await query.message.edit_text(
        text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="HELP_HOME")]]
        )
    )

    await query.answer()
