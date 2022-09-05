import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, User, Message

Client = Client(
    "service-regexlink-cleaner",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📃Source Code', url="https://github.com/MR-JINN-OF-TG/service-regexlink-cleaner")
        ]]
    ) 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, message):
    await message.reply_sticker("CAACAgUAAxkBAAEBcr1hsLH3Nu0-qQpwwWQ7FkF58xnwSgACpAMAAjieoFU-Q-udLfwBUx4E")
    await message.reply_text(
        f""" Hai {message.from_user.mention} am Service Message, command and link deleter bot.""", 
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )
@Client.on_message(filters.regex("http") | filters.regex("t.me") | filters.regex("youtu.be") | filters.regex("com") | filters.regex("https") | filters.regex("/" ) | filters.service)
async def delete(bot,message):
 await message.delete()

Client.run()
