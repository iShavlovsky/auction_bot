from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from aiogram import Bot

async def set_commands(bot:Bot, admin_ids=None):
    # Стандартные команды для всех пользователей
    common_commands = [
        BotCommand(
            command='start',
            description='Старт'
        ),
        BotCommand(
            command='marks',
            description='Все марки'
        ),
        BotCommand(
            command='marksinline',
            description='Все марки в сообщение'
        )
    ]

    await bot.set_my_commands(common_commands, scope=BotCommandScopeDefault())
    # команды только для админов
    admin_commands = common_commands + [
        BotCommand(
            command='json',
            description='JSON команда для администраторов'
        )
    ]

    for admin_id in admin_ids:
        await bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=admin_id))
