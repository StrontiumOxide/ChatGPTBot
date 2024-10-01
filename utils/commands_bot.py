from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot) -> None:
    """Данная функция добавляет меню в бота с командами ниже"""

    commands = [
        BotCommand(
            command="start",
            description="Запуск бота ▶️"
        ),
        BotCommand(
            command="start_conversation",
            description="Начать общение 💬"
        ),
        BotCommand(
            command="change_access",
            description="Изменить доступ ⚠️"
        )
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
