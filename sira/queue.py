"""
To prevent conflict with built-in modules, using "sira", the Greek word for "queue".
"""
from queue import Queue, Empty
from typing import Dict, Union

queues: Dict[int, Queue] = {}


def add(chat_id: int, file_path: str) -> int:
    if chat_id not in queues:
        queues[chat_id] = Queue()

    queues[chat_id].put({"file_path": file_path})
    return queues[chat_id].qsize()


def get(chat_id: int) -> Union[Dict[str, str], None]:
    if chat_id in queues:
        try:
            return queues[chat_id].get_nowait()
        except Empty:
            return None


def is_empty(chat_id: int) -> Union[bool, None]:
    if chat_id in queues:
        return queues[chat_id].empty()
    else:
        return True


def task_done(chat_id: int) -> None:
    if chat_id in queues:
        try:
            queues[chat_id].task_done()
        except ValueError:
            pass


def clear(chat_id: int):
    if chat_id in queues:
        if queues[chat_id].empty():
            raise Empty
        else:
            queues[chat_id].queue = []
    else:
        raise Empty
