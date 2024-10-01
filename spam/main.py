from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError
from random import randint
from functions.api_gpt import ConnectGPT
from utils.loader_token import Token
from data.loader_file import load_file


async def spamming(bot: Bot) -> None:
    """Функция по периодической рассылке"""

    query = 'Пожелай мне доброго утра, удачного дня и скажи я лучше всех. В конце напиши рандомный факт. Добавь соответствующие стикеры. Стикеры должны быть только в конце предложения.'
    
    client = ConnectGPT(GPT_TOKEN=Token(key='GPT').find())
    response = await client.send_query_gpt(query=query)

    number = randint(1,5)
    await bot.send_photo(
        chat_id=Token(key='MY_ID').find(),
        photo=load_file(
            category='photo/morning',
            filename=f'{number}.jpg'
        ),
        caption=response.get('response', 'Ничего')
    )
    