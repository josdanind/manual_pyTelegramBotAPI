"""_summary_
sendDocument: https://core.telegram.org/bots/api#senddocument

Utilice este método para enviar archivos generales. En caso de
éxito, se devuelve el mensaje enviado. Los bots actualmente
pueden enviar archivos de cualquier tipo de hasta 50 MB de
tamaño, este límite puede cambiar en el futuro.
"""
# Bot
from ...config.bot import bot
from telebot.types import Message, InputFile

path_document = "assets/papaya.pdf"
path_cover = "assets/papaya.jpeg"


async def document_command(message: Message):
    await bot.send_document(
        chat_id=message.chat.id,
        document=InputFile(path_document),
        caption="This is a manual to plant papaya",
        thumb=InputFile(path_cover),
    )
