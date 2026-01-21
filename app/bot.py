from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from app.config import BOT_TOKEN
from app.handlers.start import router as start_router
from app.handlers.tasks import router as tasks_router

def create_bot() -> Bot:
    return Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(tasks_router)
    return dp
