from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from VCPlayBot.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def bye(client, message):
    sent=0
    failed=0
    if message.from_user.id in SUDO_USERS:
        lol = await message.reply("Starting Gcast")
        if not message.reply_to_message:
            await lol.edit("Reply to any text message to gcast sir")
            return
        msg = message.reply_to_message.text
        async for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent = sent+1
                await lol.edit(f"Gcasting.. Sent: {sent} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Gcasting.. Sent: {sent} chats. Failed: {failed} chats.")
            await asyncio.sleep(3)
        await message.reply_text(f"Gcasted message to {sent} chats. Failed {failed} chats.")
