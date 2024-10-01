from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from utils.loader_token import Token

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
            command="get_id",
            description="Узнать свой id 🆔"
        ),
        BotCommand(
            command="change_access",
            description="Изменить доступ ⚠️"
        )
    ]

    await bot.set_my_commands(commands=commands[:3], scope=BotCommandScopeDefault())
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeChat(chat_id=Token(key='MY_ID').find()))
