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
    API_ID,14884817
    API_HASH,f0bc9519bd536c4c7b49c9d32a3ddc17
    bot_token=BOT_TOKEN,5109382247:AAFqHlzS_bDx0Lfkb00vLd423Qdup52UEcw
    plugins=dict(root="VCPlayBot.modules"),
)

bot.start()
run()
