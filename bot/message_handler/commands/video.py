# Bot
from ...config.bot import bot
from telebot.types import Message, InputFile

path_video = "assets/bird.mp4"


async def video_command(message: Message):
    await bot.send_chat_action(chat_id=message.chat.id, action="upload_video")
    await bot.send_video(
        chat_id=message.chat.id,
        video=InputFile(path_video),
        caption="Petirrojo europeo",
    )
