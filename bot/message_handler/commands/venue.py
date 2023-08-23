"""_summary_
sendVenue:
Utilice este método para enviar información sobre un lugar. En caso de éxito, se devuelve el mensaje enviado.
"""
# Bot
from ...config.bot import bot
from telebot.types import Message


async def venue_command(message: Message):
    chat_id = message.chat.id
    latitude, longitude = 5.17077, -72.55083

    first_location_message = await bot.send_venue(
        chat_id,
        latitude=latitude,
        longitude=longitude,
        title="Fiesta en el parque central",
        address="Parque Central",
        google_place_id="ChIJLV-lwkMYa44R83kXbbrIEWQ",
        google_place_type="park",
    )
    # Google place id:
    # https://developers.google.com/maps/documentation/places/web-service/place-id
    # Google place type:
    # https://developers.google.com/maps/documentation/places/web-service/supported_types
    # Buscar coordenadas
    # https://www.123coordenadas.com/
