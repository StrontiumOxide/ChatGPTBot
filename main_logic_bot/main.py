from aiogram import Bot, Dispatcher
from utils.commands_bot import set_commands

from utils.middlewares import CountMiddleware, CheckActiveMiddleware
from main_logic_bot.greetings import message_greetings
from main_logic_bot.dialog_gpt import message_dialog_gpt


async def main_polling(bot: Bot, dp: Dispatcher) -> None:
    """Функция, отвечающая за polling"""

        # Подключение Middleware
    dp.update.middleware(CountMiddleware())
    dp.message.middleware(CheckActiveMiddleware())

        # Список с модулями Telegram-бота
    list_modules = [

            # Приветствие
        message_greetings,

            # Диалог с ChatGPT
        message_dialog_gpt,

    ]

        # Подключение модулей
    dp.include_routers(*map(lambda file: file.router, list_modules))

        # Подключение командного меню
    await set_commands(bot=bot)

        # Polling
    await dp.start_polling(bot, polling_timeout=20)
