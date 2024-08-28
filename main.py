import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from core.handlers.base import get_start, get_message_json
from core.data.config import settings
from core.handlers.car_search import send_mark


async def start_bot(bot: Bot) -> None:
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

    dp.message.register(send_mark, F.text == '1')
    dp.message.register(get_message_json, F.text == 'json')
    dp.message.register(get_start, F.text == 'start')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(start())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен пользователем.")
