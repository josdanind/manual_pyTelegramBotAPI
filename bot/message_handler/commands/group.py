"""sendMediaGroup
- https://core.telegram.org/bots/api#sendmediagroup

- Utilice este método para enviar un grupo de fotos,
videos, documentos o audios como un álbum.
Los documentos y archivos de audio solo se pueden agrupar
en un álbum con mensajes del mismo tipo. En caso de éxito,
se de vuelve una matriz de mensajes que se enviaron.
"""
# Python
import os, re

# Bot
from ...config.bot import bot
from telebot.types import Message, InputFile, InputMediaPhoto

PATH = "assets"


async def group_command(message: Message):
    files = os.listdir(PATH)
    mediaPhotList = []

    for file_name in files:
        full_path = os.path.join("assets", file_name)

        if os.path.isfile(full_path) and re.match(r"^.+\.(jpg|jpeg)$", file_name):
            mediaPhotList.append(InputMediaPhoto(InputFile(full_path)))

    await bot.send_media_group(chat_id=message.chat.id, media=mediaPhotList)
