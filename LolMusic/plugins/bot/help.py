# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎
# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/LolMusic
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from typing import Union
from pyrogram import filters, types, enums
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton
from LolMusic import app
from LolMusic.utils import help_pannel
from LolMusic.utils.database import get_lang
from LolMusic.utils.decorators.language import LanguageStart, languageCB
from LolMusic.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers
from LolMusic.help.buttons import BUTTONS
from LolMusic.help.helper import Helper

#------------------------------------------------------------------------------------------------------------------------
# MUSIC SECTION | 🎵
#------------------------------------------------------------------------------------------------------------------------

@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(client: app, update: Union[types.Message, types.CallbackQuery]):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try: await update.answer()
        except: pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            f"✨ **{_['help_1'].format(SUPPORT_CHAT)}**", reply_markup=keyboard
        )
    else:
        try: await update.delete()
        except: pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=f"🎵 **{_['help_1'].format(SUPPORT_CHAT)}**",
            reply_markup=keyboard,
        )

@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(f"📑 **{_['help_2']}**", reply_markup=InlineKeyboardMarkup(keyboard))

@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    # Adding premium prefix to help texts
    help_text = getattr(helpers, f"HELP_{cb[2:]}")
    await CallbackQuery.edit_message_text(f"💎 **ᴍᴜsɪᴄ ʜᴇʟᴘ** 💎\n\n{help_text}", reply_markup=keyboard)

#------------------------------------------------------------------------------------------------------------------------
# MANAGEMENT SECTION | 🛡️
#------------------------------------------------------------------------------------------------------------------------

@app.on_callback_query(filters.regex("MANAGEMENT_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(f"🛡️ **{Helper.HELP_M}**", reply_markup=InlineKeyboardMarkup(BUTTONS.MBUTTON))
    
@app.on_callback_query(filters.regex('MANAGEMENT_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="MANAGEMENT_CP")]])
    if cb == "MANAGEMENT":
        await CallbackQuery.edit_message_text("❌ `Something went wrong!`", reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(f"⚙️ {getattr(Helper, cb)}", reply_markup=keyboard)

#------------------------------------------------------------------------------------------------------------------------
# TOOL SECTION | ⚡
#------------------------------------------------------------------------------------------------------------------------

@app.on_callback_query(filters.regex("TOOL_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(f"⚡ **{Helper.HELP_B}**", reply_markup=InlineKeyboardMarkup(BUTTONS.BBUTTON))

@app.on_callback_query(filters.regex('TOOL_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="TOOL_CP")]])
    if cb == "TOOL":
        await CallbackQuery.edit_message_text("❌ `Something went wrong!`", reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(f"🛠️ {getattr(Helper, cb)}", reply_markup=keyboard)

#------------------------------------------------------------------------------------------------------------------------
# MAIN HELP | 🌀
#------------------------------------------------------------------------------------------------------------------------

@app.on_callback_query(filters.regex("MAIN_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(f"✨ **{Helper.HELP_Sona}**", reply_markup=InlineKeyboardMarkup(BUTTONS.SBUTTON))

@app.on_callback_query(filters.regex('MAIN_BACK'))
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1] if len(callback_data.split(None, 1)) > 1 else "MAIN"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="MAIN_CP"), 
         InlineKeyboardButton("🔐 ᴘʀɪᴠᴀᴄʏ", url="https://telegra.ph/BOTS--PRIVACY-POLICY-01-19")]
    ])
    if cb == "MAIN":
        await CallbackQuery.edit_message_text("❌ `Something went wrong!`", reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(f"💠 {getattr(Helper, cb)}", reply_markup=keyboard)

#------------------------------------------------------------------------------------------------------------------------
# PROMOTION | 🚀
#------------------------------------------------------------------------------------------------------------------------

@app.on_callback_query(filters.regex("PROMOTION_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(f"🚀 **{Helper.HELP_PROMOTION}**", reply_markup=InlineKeyboardMarkup(BUTTONS.PBUTTON))

@app.on_callback_query(filters.regex('PROMOTION_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="PROMOTION_CP")]])
    if cb == "PROMOTION":
        await CallbackQuery.edit_message_text("❌ `Something went wrong!`", reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(f"📢 {getattr(Helper, cb)}", reply_markup=keyboard)

#------------------------------------------------------------------------------------------------------------------------
# ABOUT / PRIVACY | 🌟
#------------------------------------------------------------------------------------------------------------------------

@app.on_callback_query(filters.regex("ALLBOT_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    text = f"🌟 **ᴀʙᴏᴜᴛ {app.mention}**\n\n{Helper.HELP_ALLBOT}"
    await CallbackQuery.edit_message_text(text, reply_markup=InlineKeyboardMarkup(BUTTONS.ABUTTON))
        
@app.on_callback_query(filters.regex('ALLBOT_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="ALLBOT_CP")]])
    if cb == "ALLBOT":
        await CallbackQuery.edit_message_text("❌ `Something went wrong!`", reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(f"ℹ️ {getattr(Helper, cb)}", reply_markup=keyboard)

# ======================================================
# Premium UI Updated by Revange 😎
# ======================================================
