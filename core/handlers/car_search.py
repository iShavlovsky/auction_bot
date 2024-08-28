from typing import List

from aiogram import types, html
from core.api.api_client import CarAPI
from core.keyboards.reply import create_reply_buttons, ButtonReplyParams
from core.keyboards.inline import create_inline_buttons, ButtonInlineParams

car_api = CarAPI()

async def send_mark(message: types.Message):
    marks = car_api.get_all_marks()

    if marks:
        marka_names: List[ButtonReplyParams] = [
            {"text": mark.MARKA_NAME}
            for mark in marks
        ]
        keyboard = create_reply_buttons(marka_names, row_width=6)

        await message.answer(f"Выберите марку автомобиля! Всего {html.bold(len(marks))}.", parse_mode='HTML', reply_markup=keyboard)
    else:
        await message.answer("Не удалось получить список марок. Попробуйте позже.")


async def send_mark_inline(message: types.Message):
    marks = car_api.get_all_marks()

    if marks:
        marka_names: List[ButtonInlineParams] = [
            {"text": mark.MARKA_NAME, "callback_data": f"{mark.MARKA_ID}"}
            for mark in marks
        ]

        keyboard = create_inline_buttons(marka_names, row_width=4)

        await message.answer(f"Выберите марку автомобиля! Всего {html.bold(len(marks))}.", parse_mode='HTML', reply_markup=keyboard)
    else:
        await message.answer("Не удалось получить список марок. Попробуйте позже.")



