from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states import AddTask
from app.db import add_task, get_tasks

router = Router()

@router.message(F.text == "➕ Додати задачу")
async def add_task_start(message: Message, state: FSMContext):
    await state.set_state(AddTask.waiting_for_title)
    await message.answer("Введи назву задачі:")

@router.message(AddTask.waiting_for_title)
async def add_task_finish(message: Message, state: FSMContext):
    await add_task(message.from_user.id, message.text)
    await state.clear()
    await message.answer("✅ Задачу додано")

@router.message(F.text == "📋 Мої задачі")
async def show_tasks(message: Message):
    tasks = await get_tasks(message.from_user.id)

    if not tasks:
        await message.answer("Задач поки нема")
        return

    text = "📋 Твої задачі:\n"
    for task_id, title, done in tasks:
        status = "✅" if done else "🕒"
        text += f"{status} {task_id}. {title}\n"

    await message.answer(text)
