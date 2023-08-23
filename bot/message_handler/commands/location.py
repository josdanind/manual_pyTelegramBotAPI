# Standard Library
import time

# Bot
from ...config.bot import bot
from telebot.types import Message


async def location_command(message: Message):
    chat_id = message.chat.id
    latitude, longitude = 5.17077, -72.55083

    await bot.send_chat_action(chat_id=chat_id, action="find_location")

    first_location_message = await bot.send_location(
        chat_id, latitude=latitude, longitude=longitude, live_period=60
    )

    # Bucle para actualizar la ubicación en enviada
    for _ in range(10):
        time.sleep(3)
        latitude += 0.00005
        longitude += 0.00005

        await bot.edit_message_live_location(
            latitude=latitude,
            longitude=longitude,
            chat_id=chat_id,
            message_id=first_location_message.id,
        )
