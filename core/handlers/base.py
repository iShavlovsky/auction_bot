import json
import html as html_lib

from aiogram import Bot, html
from aiogram.types import Message

async def get_start(message: Message, bot: Bot):
    await message.answer(f'Привет {html.bold(message.from_user.full_name)}! Твой ID: {html.bold(message.from_user.id)}', parse_mode='HTML')

async def get_message_json(message: Message, bot: Bot):
    json_str = json.dumps(message.model_dump(), indent=4, ensure_ascii=False)
    max_length = 4096 - len("<pre></pre>")
    for i in range(0, len(json_str), max_length):
        part = json_str[i:i+max_length]

        await message.answer(f"<pre>{html_lib.escape(part)}</pre>", parse_mode='HTML')
