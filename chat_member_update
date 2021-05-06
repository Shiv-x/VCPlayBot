# Taken from https://github.com/callsmusic/callsmusic-1/blob/main/callsmusic/handlers/chat_member_updated.py
# Thanks to [ROJ](https://github.com/rojserbest)

# This file is a part of TG-MusicVC
# Copyright (C) 2021  Jyothis Jayanth [@EverythingSuckz]

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
