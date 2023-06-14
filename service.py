import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

app = Client(
    "Service message remover",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"]
)

START_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('SOURCE CODE', url="https://github.com/MR-JINN-OF-TG/service-regexlink-cleaner")
        ]
    ]
)


@app.on_message(filters.private & filters.command(["start"]))
async def start(_, message):
    await message.reply_sticker("CAACAgUAAxkBAAEBcr1hsLH3Nu0-qQpwwWQ7FkF58xnwSgACpAMAAjieoFU-Q-udLfwBUx4E")
    await message.reply_text(
        f"Hai {message.from_user.mention}, I am a Service Message, Command, and Link Deleter bot.",
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )


@app.on_message(filters.regex("(http|t.me|youtu.be|com|https|/)|service"))
async def delete(_, message):
    await message.delete()


app.run()
