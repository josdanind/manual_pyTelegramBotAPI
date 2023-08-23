"""_summary_
sendSticker: https://core.telegram.org/bots/api#sendsticker

Use este método para enviar pegatinas estáticas .WEBP,
.TGS animadas o .WEBM de video. En caso de éxito, se
devuelve el mensaje enviado.
"""
# Bot
from ...config.bot import bot
from telebot.types import Message, InputFile

path_sticker = "assets/Batman.webp"
path_cover = "assets/papaya.jpeg"


async def sticker_command(message: Message):
    await bot.send_sticker(
        chat_id=message.chat.id,
        sticker=InputFile(path_sticker),
    )
