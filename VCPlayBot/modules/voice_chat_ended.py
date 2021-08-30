from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

from VCPlayBot.services.callsmusic.callsmusic import remove
from VCPlayBot.helpers.channelmusic import get_chat_id


@Client.on_message(filters.voice_chat_ended)
async def voice_chat_ended(_, message: Message):
    try:
        remove(get_chat_id(message.chat))
    except Exception:
        pass
