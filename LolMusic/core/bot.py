# ©️ 2025-26 All Rights Reserved by REVANGE Bots
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus
import config
from ..logging import LOGGER

class Sona(Client):
    def __init__(self):
        LOGGER(__name__).info(f"sᴛʀᴀᴛɪɴɢ ʙᴏᴛ...")
        super().__init__(
            name="LolMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        # Logger ID Check
        if config.LOGGER_ID == 0 or config.LOGGER_ID == -100:
            LOGGER(__name__).error("LOGGER_ID set nahi hai! Please config file check karein.")
            exit()

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<u><b>» {self.mention}</u> ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :-</b>\n\n"
                    f"ɪᴅ :- <code>{self.id}</code>\n"
                    f"ɴᴀᴍᴇ :- {self.name}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ :- @{self.username}"
                ),
            )
        except errors.ChannelInvalid:
            LOGGER(__name__).error("Bot ko Log Group mein add nahi kiya gaya hai ya ID galat hai.")
            exit()
        except errors.PeerIdInvalid:
            LOGGER(__name__).error("LOGGER_ID ka format galat hai. Check karein.")
            exit()
        except Exception as ex:
            LOGGER(__name__).error(f"Unexpected Error: {ex}")
            exit()

        # Admin Check
        try:
            a = await self.get_chat_member(config.LOGGER_ID, self.id)
            if a.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error("Bot Log Group mein Admin nahi hai! Pehle admin banayein.")
                exit()
        except Exception:
            LOGGER(__name__).error("Bot ko Log Group mein message bhejne ki permission nahi hai.")
            exit()

        LOGGER(__name__).info(f"ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ ᴀs {self.name}")

    async def stop(self):
        await super().stop()
