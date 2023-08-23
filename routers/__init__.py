# FastAPI
from fastapi import APIRouter

# Routers
from .bot.webhook import router as webhook_router

router = APIRouter()
router.include_router(webhook_router)
