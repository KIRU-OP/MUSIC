# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎
# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/LolMusic
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from LolMusic import app

def help_pannel(_, START: Union[bool, int] = None):
    # Close aur Back buttons ke liye premium icons
    first = [
        InlineKeyboardButton(text=f"🗑️ {_['CLOSE_BUTTON']}", callback_data=f"close")
    ]
    second = [
        InlineKeyboardButton(text=f"🔙 {_['BACK_BUTTON']}", callback_data=f"MAIN_CP"),
    ]
    
    mark = second if START else first
    
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=f"💎 {_['H_B_1']}", callback_data="help_callback hb1"),
                InlineKeyboardButton(text=f"✨ {_['H_B_2']}", callback_data="help_callback hb2"),
                InlineKeyboardButton(text=f"🌀 {_['H_B_3']}", callback_data="help_callback hb3"),
            ],
            [
                InlineKeyboardButton(text=f"🛡️ {_['H_B_4']}", callback_data="help_callback hb4"),
                InlineKeyboardButton(text=f"⚡ {_['H_B_5']}", callback_data="help_callback hb5"),
                InlineKeyboardButton(text=f"🎙️ {_['H_B_6']}", callback_data="help_callback hb6"),
            ],
            [
                InlineKeyboardButton(text=f"🎵 {_['H_B_7']}", callback_data="help_callback hb7"),
                InlineKeyboardButton(text=f"🎬 {_['H_B_8']}", callback_data="help_callback hb8"),
                InlineKeyboardButton(text=f"🚀 {_['H_B_9']}", callback_data="help_callback hb9"),
            ],
            [
                InlineKeyboardButton(text=f"⚙️ {_['H_B_10']}", callback_data="help_callback hb10"),
                InlineKeyboardButton(text=f"📜 {_['H_B_11']}", callback_data="help_callback hb11"),
                InlineKeyboardButton(text=f"📣 {_['H_B_12']}", callback_data="help_callback hb12"),
            ],
            [
                InlineKeyboardButton(text=f"🧹 {_['H_B_13']}", callback_data="help_callback hb13"),
                InlineKeyboardButton(text=f"🌟 {_['H_B_15']}", callback_data="help_callback hb15"),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=f"🔙 {_['BACK_BUTTON']}", callback_data=f"settings_back_helper"),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=f"💡 {_['S_B_4']}", url=f"https://t.me/{app.username}?start=help")
        ],
    ]
    return buttons

# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎
# UI Updated with Premium Emojis 💎
# ======================================================
