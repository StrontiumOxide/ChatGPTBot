import asyncio

from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError
from random import choice
from utils.config import active_people

sleeping = 120


async def spamming(bot: Bot) -> None:
    """Функция по периодической рассылке"""

    while True:
        await asyncio.sleep(sleeping)

        for user_id in active_people:
            count = active_people[user_id]['count']
#             try:
#                 await bot.send_message(
#                     chat_id=user_id,
#                     text=f'⚠️ <b>{choice(advertising_phrases)}</b> ⚠️\nКстати, вы уже обратились ко мне {count} раз(а)'
#                 )
#             except TelegramForbiddenError:
#                 del active_people[user_id]


# async def cleaning_active(bot: Bot) -> None:
#     """Функция по чистке активных людей"""