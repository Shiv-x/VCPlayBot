import requests
from pyrogram import Client as Bot

from MusicXBot.config import API_HASH
from MusicXBot.config import API_ID
from MusicXBot.config import BG_IMAGE
from MusicXBot.config import BOT_TOKEN
from MusicXBot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="MusicXBot.modules"),
)

bot.start()
run()
