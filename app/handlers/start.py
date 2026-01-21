from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards import main_keyboard

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привіт! Це бот для задач 👋",
        reply_markup=main_keyboard()
    )
