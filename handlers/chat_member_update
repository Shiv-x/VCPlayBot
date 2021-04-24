from pyrogram.types import ChatMemberUpdated
from cache.admins import admins
from pyrogram import Client

@Client.on_chat_member_updated()
async def auto_admin_updater(_, chat_member_updated: ChatMemberUpdated):
    (
        admins[chat_member_updated.chat.id].append(
            chat_member_updated.new_chat_member.user.id
        )
    ) if (
        (
            (
                chat_member_updated.new_chat_member.user.id
            ) not in admins[chat_member_updated.chat.id]
        )
    ) else (
        admins[chat_member_updated.chat.id].remove(
            chat_member_updated.new_chat_member.user.id
        )
    ) if (
        (
            chat_member_updated.new_chat_member.user.id
        ) in admins[chat_member_updated.chat.id]
    ) else None
