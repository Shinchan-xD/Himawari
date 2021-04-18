
# the logging things
import logging

from pyrogram.types import Message
from youtube_search import YoutubeSearch

from Mizuki import pbot as app
from Mizuki.utils.errors import capture_err

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)



# YouTube


@app.on_message(pyrogram.filters.command(["yts"]))
@capture_err
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("/yt needs an argument")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("Searching....")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"Title - {results[i]['title']}\n"
            text += f"Duration - {results[i]['duration']}\n"
            text += f"Views - {results[i]['views']}\n"
            text += f"Channel - {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))