import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

Client = Bot(
    "service-regexlink-cleaner-bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@Bot.on_message(filters.private)
async def start(bot, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEBcr1hsLH3Nu0-qQpwwWQ7FkF58xnwSgACpAMAAjieoFU-Q-udLfwBUx4E")
    await message.reply_text(
        text=f"""Hay {message.from_user.mention} am Service Message, command and link deleter bot.""", 
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton
                        (
                            "📦 Source 📦", url="https://github.com/SpamShield/service-regexlink-cleaner"
                        )
                ]
            ]
        )
    )
@Bot.on_message(filters.regex("http") | filters.regex("t.me") | filters.regex("youtube.com") | filters.regex("youtu.be") | filters.regex("/" ) | filters.service)
async def delete(bot, message: Message):
    await message.delete()

Bot.run()
