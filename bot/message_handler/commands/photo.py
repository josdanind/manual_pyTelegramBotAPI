# Bot
from ...config.bot import bot
from telebot.types import Message

path_img = "assets/full_metal.jpg"


async def photo_command(message: Message):
    with open(path_img, "rb") as img:
        await bot.send_photo(message.chat.id, img, caption="Full Metal Alchemist")
