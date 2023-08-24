"""conversitoCommand
"""

import json
from datetime import datetime

# Bot
from ...config.bot import bot
from telebot.types import Message, ForceReply

conversation_state = "data/conversation.json"


async def conversation_command(message: Message):
    chat_id = str(message.chat.id)
    await bot.delete_message(message.chat.id, message.id)

    data: dict = json.load(open(conversation_state, "r"))
    sessions: dict = data["sessions"]

    if chat_id in sessions:
        del sessions[chat_id]

    msg = await bot.send_message(chat_id, data["questions"]["0"])

    sessions.update(
        {
            chat_id: {
                "step": 0,
                "response": {},
                "at": str(datetime.now()),
                "message_ids": [msg.id],
            }
        }
    )

    with open(conversation_state, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def check_session(message: Message):
    chat_id = str(message.chat.id)

    with open(conversation_state, "r") as f:
        data = json.load(f)
        sessions = data["sessions"]

        if chat_id in sessions:
            return True
        else:
            return False


async def process_session(message: Message):
    chat_id = message.chat.id

    data = json.load(open(conversation_state, "r"))
    session = data["sessions"][str(chat_id)]

    step = session["step"]
    session["message_ids"].append(message.id)
    questions = data["questions"]

    if step < len(questions) - 1:
        msg = await bot.send_message(chat_id, questions[str(step + 1)])

        session["step"] = step + 1
        session["response"].update({session["step"]: message.text})
        session["message_ids"].append(msg.id)
    else:
        session["response"].update({session["step"]: message.text})

        user_data = [response for response in session["response"].values()]
        msg = await bot.send_message(chat_id, abstract(user_data), "HTML")

        for msg in session["message_ids"]:
            await bot.delete_message(chat_id, msg)

        del data["sessions"][str(chat_id)]

    with open(conversation_state, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


abstract = (
    lambda msg: f"""\
<u>Información Solicitada:</u>

Nombre: <code>{msg[0]}</code>
Edad: <code>{msg[1]}</code>
hobby: <code>{msg[2]}</code>
"""
)
