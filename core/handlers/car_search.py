from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from core.api.api_client import CarAPI

car_api = CarAPI()


async def send_mark(message: types.Message):
    marks = car_api.get_all_marks()

    if marks:
        buttons = []
        for mark in marks:
            marka_name = mark.get('MARKA_NAME', '')
            marka_id = mark.get('MARKA_ID', '')
            if marka_name and marka_id:
                print(marka_name)
                print(marka_id)
                buttons.append([types.KeyboardButton(text=f"{marka_name}")])

        keyboard = types.ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True,
            input_field_placeholder="Выберите марку автомобиля"
        )
        await message.answer("Выберите марку автомобиля:", reply_markup=keyboard)
    else:
        await message.answer("Не удалось получить список марок. Попробуйте позже.")

