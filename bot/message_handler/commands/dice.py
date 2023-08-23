"""sendDice
- https://core.telegram.org/bots/api#senddice

- Utilice este método para enviar un emoji
animado que mostrará un valor aleatorio.
En caso de éxito, se devuelve el mensaje enviado.

- “🎲” (Default), “🎯”, “🏀”, “⚽”, “🎳”, or “🎰”. 

- Dice can have values 1-6 for “🎲”, “🎯” and “🎳”
values 1-5 for “🏀” and “⚽”
and values 1-64 for “🎰”.
"""
# Bot
from ...config.bot import bot
from telebot.types import Message, InputFile

path_document = "assets/papaya.pdf"
path_cover = "assets/papaya.jpeg"


async def dice_command(message: Message):
    await bot.send_dice(
        chat_id=message.chat.id,
        emoji="🎲",
    )
