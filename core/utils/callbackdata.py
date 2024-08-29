from aiogram.filters.callback_data import CallbackData


class AllMarks(CallbackData, prefix='allmarks'):
    marka: str
    id: str
