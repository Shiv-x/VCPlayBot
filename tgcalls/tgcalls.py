from pyrogram import Client
from pytgcalls.pytgcalls import PyTgCalls

import sira
import config


client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)


@pytgcalls.on_stream_end()
def on_stream_end(chat_id: int) -> None:
    sira.task_done(chat_id)

    if sira.is_empty(chat_id):
        pytgcalls.leave_group_call(chat_id)
    else:
        pytgcalls.change_stream(
            chat_id, sira.get(chat_id)["file_path"]
        )


run = pytgcalls.run
