from pyrogram import Client as Bot
from .config import API_ID, API_HASH, BOT_TOKEN
from .videoplayer import app

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=videoplayer,
)

bot.start()
app.start()
