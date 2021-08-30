from typing import Dict

from pytgcalls import GroupCallFactory

from VCPlayBot.services.callsmusic import client
from VCPlayBot.services.queues import queues


instances: Dict[int, GroupCallFactory] = {}
active_chats: Dict[int, Dict[str, bool]] = {}


def init_instance(chat_id: int):
    if chat_id not in instances:
        instances[chat_id] = GroupCallFactory(client,outgoing_audio_bitrate_kbit=512).get_file_group_call()

    instance = instances[chat_id]

    @instance.on_playout_ended
    async def ___(__, _):
        queues.task_done(chat_id)

        if queues.is_empty(chat_id):
            await stop(chat_id)
        else:
            instance.input_filename = queues.get(chat_id)["file_path"]


def remove(chat_id: int):
    if chat_id in instances:
        del instances[chat_id]

    if not queues.is_empty(chat_id):
        queues.clear(chat_id)

    if chat_id in active_chats:
        del active_chats[chat_id]


def get_instance(chat_id: int) -> GroupCallFactory:
    init_instance(chat_id)
    return instances[chat_id]


async def start(chat_id: int):
    await get_instance(chat_id).start(chat_id)
    active_chats[chat_id] = {"playing": True, "muted": False}


async def stop(chat_id: int):
    await get_instance(chat_id).stop()

    if chat_id in active_chats:
        del active_chats[chat_id]


async def set_stream(chat_id: int, file: str):
    if chat_id not in active_chats:
        await start(chat_id)
    get_instance(chat_id).input_filename = file


def pause(chat_id: int) -> bool:
    if chat_id not in active_chats:
        return False
    elif not active_chats[chat_id]["playing"]:
        return False

    get_instance(chat_id).pause_playout()
    active_chats[chat_id]["playing"] = False
    return True


def resume(chat_id: int) -> bool:
    if chat_id not in active_chats:
        return False
    elif active_chats[chat_id]["playing"]:
        return False

    get_instance(chat_id).resume_playout()
    active_chats[chat_id]["playing"] = True
    return True


async def mute(chat_id: int) -> int:
    if chat_id not in active_chats:
        return 2
    elif active_chats[chat_id]["muted"]:
        return 1

    await get_instance(chat_id).set_is_mute(True)
    active_chats[chat_id]["muted"] = True
    return 0


async def unmute(chat_id: int) -> int:
    if chat_id not in active_chats:
        return 2
    elif not active_chats[chat_id]["muted"]:
        return 1

    await get_instance(chat_id).set_is_mute(False)
    active_chats[chat_id]["muted"] = False
    return 0
