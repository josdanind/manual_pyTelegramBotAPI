# Standard Library
import json

# FastAPI
from fastapi import APIRouter, Request, status, HTTPException

# Bot
from bot import bot
import telebot.async_telebot as telebot

router = APIRouter(prefix="/bot")


@router.post(path="/webhook", status_code=status.HTTP_200_OK)
async def webhook(request: Request):
    if request.headers["content-type"] == "application/json":
        try:
            data = await request.json()
            async_update = telebot.types.Update.de_json(json.dumps(data))

            await bot.process_new_updates([async_update])
        except Exception as e:
            print("Error al procesar las actualizaciones.")
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Contenido no válido",
        )
