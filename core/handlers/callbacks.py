from aiogram.types import CallbackQuery

from core.utils import AllMarks


async def selected_id_mark(call: CallbackQuery, callback_data:AllMarks):
    id = callback_data.id
    marka = callback_data.marka
    answer = f'{call.message.from_user.first_name}, ты выбрал марку {marka}, её ID {id}'

    await call.message.answer(answer)
    await call.answer()
