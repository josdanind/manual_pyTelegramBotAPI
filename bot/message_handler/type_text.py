# Bot
from ..config.bot import bot
from telebot.types import Message

welcome_message = lambda username: f"Hola {username}, bienvenido a este grupo"


async def text(message) -> int:
    message_data = await bot.reply_to(message, message.text)
    return message_data.message_id


async def new_member(message: Message) -> None:
    chat_id = message.chat.id
    for new_member in message.new_chat_members:
        username = new_member.username
        bot.send_message(chat_id=chat_id, text=welcome_message(username))
