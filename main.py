import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command

from core.data import settings
from core.handlers import get_start, send_mark, send_mark_inline, selected_id_mark, get_message_json
from core.utils import set_commands, AllMarks


async def start_bot(bot: Bot) -> None:
    await set_commands(bot, settings.bots.admin_ids)
    for admin_id in settings.bots.admin_ids:
        await bot.send_message(chat_id=admin_id, text='Бот запущен')

async def stop_bot(bot: Bot) -> None:
    for admin_id in settings.bots.admin_ids:
        await bot.send_message(chat_id=admin_id, text='Бот остановлен')

async def start() -> None:
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )

    bot = Bot(
        token=settings.bots.bot_token,
        defaults=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_start, F.text == 'start')

    dp.message.register(send_mark, Command(commands=['allmarks', 'marks']))
    dp.message.register(send_mark, F.text == 'marks')

    dp.message.register(send_mark_inline, Command(commands=['allmarksinline', 'marksinline']))
    dp.message.register(send_mark_inline, F.text == 'marksinline')
    dp.callback_query.register(selected_id_mark, AllMarks.filter())

    dp.message.register(get_message_json, F.text == 'json')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(start())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен пользователем.")
