import requests
from pyrogram import Client as Bot

from MusicBot.config import APP_HASH, APP_ID, BG_IMAGE, BOT_TOKEN
from MusicBot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    APP_ID,
    APP_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="MusicBot.modules"),
)

run()
