import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from utils.loader_token import Token

from main_logic_bot.main import main_polling
from spam.main import spamming
from asset_cleanup.main import cleaning

logging.basicConfig(level=logging.ERROR, filename='bot_log.log', filemode='a', encoding='utf-8')


async def main():
    """Главная функция"""

    bot = Bot(token=Token(key='T').find(), parse_mode=ParseMode.HTML)
    dp = Dispatcher()

        # Отложенный запуск уведомления
    scheduler = AsyncIOScheduler()
    scheduler.add_job(spamming, 'cron', hour=8, minute=0, args=[bot])
    scheduler.start()

    try:
            # Уведомление о запуске Telegram-бота
        await bot.send_message(
            chat_id=Token(key='MY_ID').find(),
            text='<b>[INFO] Telegram-бот запущен!</b>'
        )
    except TelegramBadRequest:
        print('[INFO] Telegram-бот запущен!')

        # Сбор всех корутин
    await asyncio.gather(
        main_polling(bot=bot, dp=dp),
        cleaning()
    )


if __name__ == "__main__":
    asyncio.run(main())
