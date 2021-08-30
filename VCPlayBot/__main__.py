import requests
from pyrogram import Client as Bot

from VCPlayBot.config import API_HASH
from VCPlayBot.config import API_ID
from VCPlayBot.config import BG_IMAGE
from VCPlayBot.config import BOT_TOKEN
from VCPlayBot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="VCPlayBot.modules"),
)

bot.start()
run()
