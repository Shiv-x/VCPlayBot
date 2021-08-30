
from os import path

from youtube_dl import YoutubeDL

from VCPlayBot.config import DURATION_LIMIT
from VCPlayBot.helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "verbose": True,
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}

ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"🛑 Videos longer than {DURATION_LIMIT} minute(s) aren't allowed, "
            f"the provided video is {duration} minute(s)",
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"🛑 Videos longer than {DURATION_LIMIT} minute(s) aren't allowed, "
            f"the provided video is {duration} minute(s)",
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
