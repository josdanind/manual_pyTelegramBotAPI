"""_summary_
sendPoll: https://core.telegram.org/bots/api#sendpoll
Utilice este método para enviar una encuesta nativa. En caso de éxito, se devuelve el mensaje enviado.
"""
# Bot
from ...config.bot import bot
from telebot.types import Message


async def poll_command(message: Message):
    chat_id = message.chat.id
    # Encuesta anónima
    # await bot.send_poll(
    #     chat_id=chat_id, question="Entendiste el método?", options=["Si", "No"]
    # )

    # Encuesta no anónima
    # await bot.send_poll(
    #     chat_id=chat_id,
    #     question="Entendiste el método?",
    #     options=["Si", "No"],
    #     is_anonymous=False,
    # )

    # Encuesta con multiple respuesta
    # await bot.send_poll(
    #     chat_id=chat_id,
    #     question="Entendiste el método?",
    #     options=["Si", "No"],
    #     is_anonymous=False,
    #     allows_multiple_answers=True,
    # )

    # Encuesta tipo quiz
    await bot.send_poll(
        chat_id=chat_id,
        question="Es Daniel el mejor programador?",
        options=["Si", "No"],
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        explanation="El nunca se rindió.",
        open_period=20,
    )
