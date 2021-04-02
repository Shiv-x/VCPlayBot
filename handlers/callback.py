from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

from tgcalls import pytgcalls


@Client.on_callback_query(filters.regex("close"))
async def close(client: Client, query: CallbackQuery):
    await query.message.delete()
