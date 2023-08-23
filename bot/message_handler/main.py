# Bot
from ..config.bot import bot
from telebot.types import Message

# Commands handler
from .commands.main import (
    commands,
    start_command,
    photo_command,
    audio_command,
    video_command,
    location_command,
    venue_command,
    poll_command,
    document_command,
    sticker_command,
    dice_command,
    group_command,
)

# Text Handler
from .type_text import text, new_member

"""
En un chat de grupo, solo sae pueden recibir
comandos, no texto.
"""

set_commands = [
    ("dice", "Iniciar juego"),
]


# *******************
# * Command Handler *
# *******************
@bot.message_handler(commands=commands)
async def command_handler(message: Message):
    msg_text = message.text.split()
    command = msg_text[0]
    args = msg_text[1:]

    match command:
        case "/start":
            if args:
                await start_command(message, args=args)
            else:
                await start_command(message)
        case "/photo":
            await photo_command(message)
        case "/audio":
            await audio_command(message)
        case "/video":
            await video_command(message)
        case "/location":
            await location_command(message)
        case "/venue":
            await venue_command(message)
        case "/poll":
            await poll_command(message)
        case "/document":
            await document_command(message)
        case "/sticker":
            await sticker_command(message)
        case "/dice":
            await dice_command(message)
        case "/group":
            await group_command(message)


"""
content_types: 'text', 'audio', 'document', 'photo',
'sticker', 'video', 'voice', 'video_note', 'location',
'contact' y 'new_chat_members'
"""


# ****************
# * Text Handler *
# ****************
# Definir el controlador de mensajes con filtrado
@bot.message_handler(func=lambda message: message.text and "axs" in message.text)
async def handle_filtered_message(message: Message):
    await bot.reply_to(message, "¡Has mencionado la palabra clave!")


# Controlador usando expresiones regulares
@bot.message_handler(regexp=r"python")
async def handle_filtered_message(message: Message):
    await bot.reply_to(message, "¡Python es genial! 🐍")


@bot.message_handler(func=lambda message: True, content_types=["text"])
async def text_handler(message: Message):
    await text(message)
