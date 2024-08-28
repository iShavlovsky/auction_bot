from aiogram.types import WebAppInfo, InlineKeyboardButton, LoginUrl
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import List, Optional, Union, Tuple, TypedDict


class ButtonInlineParams(TypedDict, total=False):
    text: str
    url: Optional[str]
    callback_data: Optional[str]
    web_app: Optional[WebAppInfo]
    login_url: Optional[LoginUrl]
    switch_inline_query: Optional[str]
    switch_inline_query_current_chat: Optional[str]
    switch_inline_query_chosen_chat: Optional[str]
    callback_game: Optional[str]
    pay: Optional[bool]

def create_inline_buttons(
        items:List[ButtonInlineParams],
        row_width: Union[int, Tuple[int, int, int]] = 1,
        placeholder="Выберите опцию"):
    keyboard_builder = InlineKeyboardBuilder()

    for item in items:
        keyboard_builder.button(**item)

    if isinstance(row_width, int):
        keyboard_builder.adjust(row_width)
    else:
        keyboard_builder.adjust(*row_width)

    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
        selective=True,
        input_field_placeholder=placeholder
    )
