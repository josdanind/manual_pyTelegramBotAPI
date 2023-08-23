# Bot
from ...config.bot import bot
from telebot.types import Message


def welcome_message(name=""):
    name = f" {name}" if name else name
    return f"<b><u>Hola{name}, bienvenido al Bot</u></b>"


async def start_command(message: Message, args: list = []):
    name = " ".join(args)
    print(welcome_message())
    await bot.send_message(message.chat.id, welcome_message(name), parse_mode="HTML")
