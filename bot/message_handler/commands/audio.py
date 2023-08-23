# Bot
from ...config.bot import bot
from telebot.types import Message, InputFile

path_mp3 = "assets/lion.mp3"
path_cover = "assets/lion.jpg"


async def audio_command(message: Message):
    await bot.send_audio(
        chat_id=message.chat.id,
        audio=InputFile(path_mp3),
        caption="The sound is that of a lion",
        thumb=InputFile(path_cover),
    )
