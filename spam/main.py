import asyncio

from aiogram import Bot
from random import choice
from utils.config import active_people

sleeping = 120


async def spamming(bot: Bot) -> None:
    """Функция по периодической рассылке"""

    while True:
        await asyncio.sleep(sleeping)

        advertising_phrases = [
            "Ваш идеальный стиль начинается здесь!",
            "Не упустите шанс изменить свою жизнь сегодня!",
            "Качество, которое вы можете доверять!",
            "Специальное предложение: только сегодня скидка 50%!",
            "Откройте для себя мир возможностей с нашим продуктом!",
            "Удобство и стиль в каждой детали!",
            "Сделайте шаг к лучшему будущему вместе с нами!",
            "Пока вы спите, мы работаем над вашим комфортом!",
            "Ваше счастье — наша первоочередная задача!",
            "Покупая у нас, вы инвестируете в качество!"
        ]

        for user_id in active_people:
            count = active_people[user_id]['count']
            await bot.send_message(
                chat_id=user_id,
                text=f'⚠️ <b>{choice(advertising_phrases)}</b> ⚠️\nКстати, вы уже обратились ко мне {count} раз(а)'
            )
