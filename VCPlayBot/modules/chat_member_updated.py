from pyrogram import Client
from pyrogram.types import ChatMemberUpdated

from VCPlayBot.function import *


@Client.on_chat_member_updated()
async def chat_member_updated(_, chat_member_updated: ChatMemberUpdated):
    if chat_member_updated.new_chat_member and chat_member_updated.old_chat_member:
        (
            admins.admins[chat_member_updated.chat.id].append(
                chat_member_updated.new_chat_member.user.id,
            )
        ) if (
            (chat_member_updated.new_chat_member.can_manage_voice_chats)
            and (
                (chat_member_updated.new_chat_member.user.id)
                not in admins.admins[chat_member_updated.chat.id]
            )
        ) else (
            admins.admins[chat_member_updated.chat.id].remove(
                chat_member_updated.new_chat_member.user.id,
            )
        ) if (
            (chat_member_updated.new_chat_member.user.id)
            in admins.admins[chat_member_updated.chat.id]
        ) else None
