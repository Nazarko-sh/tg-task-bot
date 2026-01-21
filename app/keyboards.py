from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Додати задачу")],
            [KeyboardButton(text="📋 Мої задачі")]
        ],
        resize_keyboard=True
    )
