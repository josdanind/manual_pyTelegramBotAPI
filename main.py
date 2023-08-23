# Fastapi
from fastapi import FastAPI

# Routers
from routers import router

# Bot
from bot import bot

# Utils
from utils.ngrok import init_ngrok

# Environment variables
from config import NGROK_TOKEN


api = FastAPI(title="pyTelegramBotAPI")
api.include_router(router)


@api.on_event("startup")
async def startup():
    api_url = init_ngrok(NGROK_TOKEN) + "/bot/webhook"

    await bot.set_webhook(api_url)
