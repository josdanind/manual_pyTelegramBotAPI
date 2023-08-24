# Standard Library
import json

# FastAPI
from fastapi import APIRouter, Request, status, HTTPException

# Bot
from bot import bot
import telebot.async_telebot as telebot

router = APIRouter(prefix="/bot")

welcome_message = lambda username: f"Hola {username}, bienvenido a este grupo"


@router.post(path="/webhook", status_code=status.HTTP_200_OK)
async def webhook(request: Request):
    if request.headers["content-type"] == "application/json":
        try:
            data = await request.json()
            message = []

            if "message" in data:
                message = data["message"]

            async_update = telebot.types.Update.de_json(json.dumps(data))

            await bot.process_new_updates([async_update])

            if "new_chat_members" in message:
                chat_id = message["chat"]["id"]
                new_users = message["new_chat_members"]

                for user in new_users:
                    await bot.send_message(chat_id, welcome_message(user["first_name"]))

        except Exception as e:
            print("Error al procesar las actualizaciones.")
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Contenido no válido",
        )
