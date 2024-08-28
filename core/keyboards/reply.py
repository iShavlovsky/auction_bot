from typing import Union, Tuple, TypedDict, Optional, List

from aiogram.types import KeyboardButtonRequestUsers, KeyboardButtonRequestChat, \
    KeyboardButtonPollType, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

class ButtonReplyParams(TypedDict, total=False):
    text: str
    request_users: Optional[KeyboardButtonRequestUsers]
    request_chat: Optional[KeyboardButtonRequestChat]
    request_contact: Optional[bool]
    request_location: Optional[bool]
    request_poll: Optional[KeyboardButtonPollType]
    web_app: Optional[WebAppInfo]

def create_reply_buttons(
        items:List[ButtonReplyParams],
        row_width: Union[int, Tuple[int, int, int]] = 1,
        placeholder="Выберите опцию"):
    keyboard_builder = ReplyKeyboardBuilder()

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
