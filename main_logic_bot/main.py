from aiogram import Bot, Dispatcher
from utils.commands_bot import set_commands

from utils.middlewares import CountMiddleware, CheckActiveMiddleware
from main_logic_bot.greetings import message_greetings
from main_logic_bot.dialog_gpt import message_dialog_gpt
from main_logic_bot.change_access import message_change_access, callback_query_change_access
from main_logic_bot.get_id import message_get_id
from main_logic_bot.unload_log import message_unload


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

            # Изменение доступа
        message_change_access,
        callback_query_change_access,

            # Получение своего id
        message_get_id,

            # Выгрузка log
        message_unload
    ]

        # Подключение модулей
    dp.include_routers(*map(lambda file: file.router, list_modules))

        # Подключение командного меню
    await set_commands(bot=bot)

        # Удаление вебхуков
    await bot.delete_webhook(drop_pending_updates=True) 

        # Polling
    await dp.start_polling(bot, polling_timeout=20)
