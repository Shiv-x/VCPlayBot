"""

    tgvc-userbot, Telegram Voice Chat Userbot
    Copyright (C) 2021  Dash Eclipse

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

Play and Control Audio playing in Telegram Voice Chat

Dependencies:
- ffmpeg

Required group admin permissions:
- Delete messages
- Manage voice chats (optional)

How to use:
- Start the userbot
- send !join to a voice chat enabled group chat
  from userbot account itself or its contacts
- reply to an audio with /play to start playing
  it in the voice chat, every member of the group
  can use the !play command now
- check !help for more commands
"""

import asyncio
import os
from datetime import datetime, timedelta

from pyrogram import Client, filters, emoji
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR
from pyrogram.types import Message

from utils.filters import main_filter, self_or_contact_filter
from utils.vc import mp

DELETE_DELAY = 8
DURATION_AUTOPLAY_MIN = 10
DURATION_PLAY_HOUR = 3

USERBOT_HELP = f"""{emoji.LABEL}  **Common Commands**:
__available to group members of current voice chat__
__starts with / (slash) or ! (exclamation mark)__

\u2022 **/play**  reply with an audio to play/queue it, or show playlist
\u2022 **/current**  show current playing time of current track
\u2022 **/repo**  show git repository of the userbot
\u2022 `!help`  show help for commands


{emoji.LABEL}  **Admin Commands**:
__available to userbot account itself and its contacts__
__starts with ! (exclamation mark)__

\u2022 `!skip` [n] ...  skip current or n where n >= 2
\u2022 `!join`  join voice chat of current group
\u2022 `!leave`  leave current voice chat
\u2022 `!vc`  check which VC is joined
\u2022 `!stop`  stop playing
\u2022 `!replay`  play from the beginning
\u2022 `!clean`  remove unused RAW PCM files
\u2022 `!pause` pause playing
\u2022 `!resume` resume playing
\u2022 `!mute`  mute the VC userbot
\u2022 `!unmute`  unmute the VC userbot
"""

USERBOT_REPO = f"""{emoji.ROBOT} **Telegram Voice Chat UserBot**

- Repository: [GitHub](https://github.com/callsmusic/tgvc-userbot)
- License: AGPL-3.0-or-later"""


# - Pyrogram filters


async def current_vc_filter(_, __, m: Message):
    group_call = mp.group_call
    if not group_call.is_connected:
        return False
    chat_id = int("-100" + str(group_call.full_chat.id))
    if m.chat.id == chat_id:
        return True
    return False


current_vc = filters.create(current_vc_filter)


# - Pyrogram handlers


@Client.on_message(
    filters.group
    & ~filters.edited
    & current_vc
    & (filters.regex("^(\\/|!)play$") | filters.audio)
)
async def play_track(client, m: Message):
    group_call = mp.group_call
    playlist = mp.playlist
    # check audio
    if m.audio:
        if m.audio.duration > (DURATION_AUTOPLAY_MIN * 60):
            reply = await m.reply_text(
                f"{emoji.ROBOT} audio which duration longer than "
                f"{str(DURATION_AUTOPLAY_MIN)} min won't be automatically "
                "added to playlist"
            )
            await _delay_delete_messages((reply,), DELETE_DELAY)
            return
        m_audio = m
    elif m.reply_to_message and m.reply_to_message.audio:
        m_audio = m.reply_to_message
        if m_audio.audio.duration > (DURATION_PLAY_HOUR * 60 * 60):
            reply = await m.reply_text(
                f"{emoji.ROBOT} audio which duration longer than "
                f"{str(DURATION_PLAY_HOUR)} hours won't be added to playlist"
            )
            await _delay_delete_messages((reply,), DELETE_DELAY)
            return
    else:
        await mp.send_playlist()
        await m.delete()
        return
    # check already added
    if playlist and playlist[-1].audio.file_unique_id \
            == m_audio.audio.file_unique_id:
        reply = await m.reply_text(f"{emoji.ROBOT} already added")
        await _delay_delete_messages((reply, m), DELETE_DELAY)
        return
    # add to playlist
    playlist.append(m_audio)
    if len(playlist) == 1:
        m_status = await m.reply_text(
            f"{emoji.INBOX_TRAY} downloading and transcoding..."
        )
        await mp.download_audio(playlist[0])
        group_call.input_filename = os.path.join(
            client.workdir,
            DEFAULT_DOWNLOAD_DIR,
            f"{playlist[0].audio.file_unique_id}.raw"
        )
        await mp.update_start_time()
        await m_status.delete()
        print(f"- START PLAYING: {playlist[0].audio.title}")
    await mp.send_playlist()
    for track in playlist[:2]:
        await mp.download_audio(track)
    if not m.audio:
        await m.delete()


@Client.on_message(main_filter
                   & current_vc
                   & filters.regex("^(\\/|!)current$"))
async def show_current_playing_time(_, m: Message):
    start_time = mp.start_time
    playlist = mp.playlist
    if not start_time:
        reply = await m.reply_text(f"{emoji.PLAY_BUTTON} unknown")
        await _delay_delete_messages((reply, m), DELETE_DELAY)
        return
    utcnow = datetime.utcnow().replace(microsecond=0)
    if mp.msg.get('current') is not None:
        await mp.msg['current'].delete()
    mp.msg['current'] = await playlist[0].reply_text(
        f"{emoji.PLAY_BUTTON}  {utcnow - start_time} / "
        f"{timedelta(seconds=playlist[0].audio.duration)}",
        disable_notification=True
    )
    await m.delete()


@Client.on_message(main_filter
                   & (self_or_contact_filter | current_vc)
                   & filters.regex("^(\\/|!)help$"))
async def show_help(_, m: Message):
    if mp.msg.get('help') is not None:
        await mp.msg['help'].delete()
    mp.msg['help'] = await m.reply_text(USERBOT_HELP, quote=False)
    await m.delete()


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.command("skip", prefixes="!"))
async def skip_track(_, m: Message):
    playlist = mp.playlist
    if len(m.command) == 1:
        await mp.skip_current_playing()
    else:
        try:
            items = list(dict.fromkeys(m.command[1:]))
            items = [int(x) for x in items if x.isdigit()]
            items.sort(reverse=True)
            text = []
            for i in items:
                if 2 <= i <= (len(playlist) - 1):
                    audio = f"[{playlist[i].audio.title}]({playlist[i].link})"
                    playlist.pop(i)
                    text.append(f"{emoji.WASTEBASKET} {i}. **{audio}**")
                else:
                    text.append(f"{emoji.CROSS_MARK} {i}")
            reply = await m.reply_text("\n".join(text))
            await mp.send_playlist()
        except (ValueError, TypeError):
            reply = await m.reply_text(f"{emoji.NO_ENTRY} invalid input",
                                       disable_web_page_preview=True)
        await _delay_delete_messages((reply, m), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & filters.regex("^!join$"))
async def join_group_call(client, m: Message):
    group_call = mp.group_call
    group_call.client = client
    if group_call.is_connected:
        await m.reply_text(f"{emoji.ROBOT} already joined a voice chat")
        return
    await group_call.start(m.chat.id)
    await m.delete()


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!leave$"))
async def leave_voice_chat(_, m: Message):
    group_call = mp.group_call
    mp.playlist.clear()
    group_call.input_filename = ''
    await group_call.stop()
    await m.delete()


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & filters.regex("^!vc$"))
async def list_voice_chat(client, m: Message):
    group_call = mp.group_call
    if group_call.is_connected:
        chat_id = int("-100" + str(group_call.full_chat.id))
        chat = await client.get_chat(chat_id)
        reply = await m.reply_text(
            f"{emoji.MUSICAL_NOTES} **currently in the voice chat**:\n"
            f"- **{chat.title}**"
        )
    else:
        reply = await m.reply_text(emoji.NO_ENTRY
                                   + "didn't join any voice chat yet")
    await _delay_delete_messages((reply, m), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!stop$"))
async def stop_playing(_, m: Message):
    group_call = mp.group_call
    group_call.stop_playout()
    reply = await m.reply_text(f"{emoji.STOP_BUTTON} stopped playing")
    await mp.update_start_time(reset=True)
    mp.playlist.clear()
    await _delay_delete_messages((reply, m), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!replay$"))
async def restart_playing(_, m: Message):
    group_call = mp.group_call
    if not mp.playlist:
        return
    group_call.restart_playout()
    await mp.update_start_time()
    reply = await m.reply_text(
        f"{emoji.COUNTERCLOCKWISE_ARROWS_BUTTON}  "
        "playing from the beginning..."
    )
    await _delay_delete_messages((reply, m), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!pause"))
async def pause_playing(_, m: Message):
    mp.group_call.pause_playout()
    await mp.update_start_time(reset=True)
    reply = await m.reply_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} paused",
                               quote=False)
    mp.msg['pause'] = reply
    await m.delete()


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!resume"))
async def resume_playing(_, m: Message):
    mp.group_call.resume_playout()
    reply = await m.reply_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} resumed",
                               quote=False)
    if mp.msg.get('pause') is not None:
        await mp.msg['pause'].delete()
    await m.delete()
    await _delay_delete_messages((reply,), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!clean$"))
async def clean_raw_pcm(client, m: Message):
    download_dir = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR)
    all_fn: list[str] = os.listdir(download_dir)
    for track in mp.playlist[:2]:
        track_fn = f"{track.audio.file_unique_id}.raw"
        if track_fn in all_fn:
            all_fn.remove(track_fn)
    count = 0
    if all_fn:
        for fn in all_fn:
            if fn.endswith(".raw"):
                count += 1
                os.remove(os.path.join(download_dir, fn))
    reply = await m.reply_text(f"{emoji.WASTEBASKET} cleaned {count} files")
    await _delay_delete_messages((reply, m), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!mute$"))
async def mute(_, m: Message):
    group_call = mp.group_call
    group_call.set_is_mute(True)
    reply = await m.reply_text(f"{emoji.MUTED_SPEAKER} muted")
    await _delay_delete_messages((reply, m), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!unmute$"))
async def unmute(_, m: Message):
    group_call = mp.group_call
    group_call.set_is_mute(False)
    reply = await m.reply_text(f"{emoji.SPEAKER_MEDIUM_VOLUME} unmuted")
    await _delay_delete_messages((reply, m), DELETE_DELAY)


@Client.on_message(main_filter
                   & current_vc
                   & filters.regex("^(\\/|!)repo$"))
async def show_repository(_, m: Message):
    if mp.msg.get('repo') is not None:
        await mp.msg['repo'].delete()
    mp.msg['repo'] = await m.reply_text(
        USERBOT_REPO,
        disable_web_page_preview=True,
        quote=False
    )
    await m.delete()


# - Other functions

async def _delay_delete_messages(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for m in messages:
        await m.delete()
