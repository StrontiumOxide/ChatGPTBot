from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from functions.api_gpt import ConnectGPT
from utils.loader_token import Token
from random import randint
from data.loader_file import load_file

query_morning = '''
Мне необходимо, чтобы ты пожелал мне доброе утро, сказал что сегодня прекрасный день
для новых свершений, сказал чтобы я не переживал из-за пустяков и сказал, что я лучше всех.
В конце напиши случайный факт из таких областей как РЖД, медицина, программирование, фанфики. 
В конец каждого предложения подбери соответствующий смайлик.
Текст расположи красиво по абзацам. Напиши не совсем кратко, но и не слишком много.
'''

query_night = '''
Мне необходимо, чтобы ты пожелал мне спокойной ночи, сказал что я высплюсь этой ночью,
то что мне приснятся красивые сны и новый день будет чудесным и прекрасным. 
В конец каждого предложения подбери соответствующий смайлик.
Текст расположи красиво по абзацам. Напиши не совсем кратко, но и не слишком много.
'''


async def spamer(bot: Bot, time: str) -> None:
    """Фунция по рассылке сообщений"""

    list_ids = [
        Token(key='MY_ID').find(),
        Token(key='HER_ID').find()
    ]

    if time == 'morning':
        query = query_morning
    elif time == 'night':
        query = query_night
    
    client = ConnectGPT(gpt_token=Token(key='GPT').find())
    response = await client.send_query_gpt(query=query)

    if response == None:
        return
    elif response.get('is_success'):
        text = response.get('response')
    else:
        return
    
    for user_id in list_ids:
        try:
            await bot.send_photo(
                chat_id=user_id,
                photo=load_file(
                    category=f'photo/{time}',
                    filename=f'{randint(1,5)}.jpg'
                ),
                caption=text
            )
        except (TelegramBadRequest, TelegramForbiddenError):
            pass
