from aiogram import Router, types as tp
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest
from time import time as timer
from random import choice
from main_logic_bot.greetings import kb_greetings as kb
from utils.states import DialogGPTState
from functions.api_gpt import ConnectGPT

from main_logic_bot.dialog_gpt import kb_dialog_gpt as kb

router = Router(name='message_dialog_gpt')


async def check_text(message: tp.Message) -> bool | None:
    """Функция по проверке наличия текста в сообщении"""

    if not message.text:
        await message.answer(text='Извините, в вашем сообщении нет текста 😒')
        return True
    

async def check_content(message: tp.Message, state: FSMContext) -> bool | None:
    """Функция встречает ключевого слово и останавливает общение с ChatGPT"""

    text = f'''
⚠️ <b>Диалог завершён!</b> ⚠️
Возвращайтесь ещё!
'''
    
    if message.text == 'Прекратить общение ❌':
        await message.answer(
            text=text,
            reply_markup=kb.reply.remove
        )

        await state.clear()
        return True


@router.message(Command(commands=['start_conversation']))
async def start_conversation_handler(message: tp.Message, state: FSMContext) -> None:
    """Функция по обработке команды /start_conversation"""

    text = f'''
⚠️ <b>Начало диалога!</b> ⚠️

Чтобы ChatGPTBot предоставлял более качественные ответы, важно определить его роль в беседе. 💬

Это повысит продуктивность и интерес общения. ℹ️

Вы можете выбрать одну из ролей или предложить свою, чтобы ChatGPTBot лучше понял ваши ожидания и сделало диалог более комфортным и увлекательным. 🥳 

Давайте сделаем наше взаимодействие интересным! ⬇️
'''
    
    await message.answer(
        text=text,
        reply_markup=kb.reply.create_kb_profeccion()
    )

    await state.set_state(DialogGPTState.role)


@router.message(DialogGPTState.role)
async def get_role(message: tp.Message, state: FSMContext) -> None:
    """Функция по получению роли для ChatGPT"""

        # Проверка наличия текста в сообщении
    if await check_text(message=message): return

        # Проверка на завершение общения
    if await check_content(message=message, state=state): return
    
    # await state.update_data(role=message.text)

    random_word = choice(['Отлично!', 'Замечательно!', 'Прекрасный выбор!', 'Так держать!'])
    text = f'''
{random_word} 🥳

Роль ChatGPT - <b>{message.text}</b>

ИИ ожидает вас❗️ Приятного общения 😌
'''

    await message.answer(
        text=text,
        reply_markup=kb.reply.cancel_request
    )

    await state.update_data(history=[{'role': "user", 'content': f'Твоя роль: {message.text}. Уровень твоих знаний самый высокий!'}])
    await state.set_state(DialogGPTState.request)


@router.message(DialogGPTState.request)
async def get_request(message: tp.Message, state: FSMContext) -> None:
    """Функция по получению запросов от пользователя. Передача ChatGPT"""

        # Проверка наличия текста в сообщении
    if await check_text(message=message): return

        # Проверка на завершение общения
    if await check_content(message=message, state=state): return

    await send_request(message=message, state=state)


async def send_request(message: tp.Message, state: FSMContext) -> None:
    """Функция по отправке запроса на сервера ChatGPT"""

    data: dict = await state.get_data()
    history: list = data.get('history')

    msg = await message.answer(
        text='<b>ChatGPT</b> генерирует ответ...'
    )

    start_time = timer()

        # Отправка запроса серверам ChatGPT
    client = ConnectGPT(GPT_TOKEN='chad-007cca7c7747490093ce6f7958b050a3c3bbt0xn')
    response = await client.send_query_gpt(query=message.text, history=history)

    delta_time = round(timer() - start_time, 2)  

    await answer_user(
        message=msg,
        state=state,
        query=message.text,
        response=response,
        delta_time=delta_time,
        history=history
    )


async def answer_user(message: tp.Message, state: FSMContext, query: str, response: dict, delta_time: int, history: list) -> None:
    """Функция по отправке ответа пользователю"""

    if response == None:
        response_text = '''Прошу прощения, я не смог подключиться к серверам ChatGPT 😞
Попробуйте ещё 😉'''

    elif response.get('is_success'):
        response_text = response.get('response')

        history.append(
            {'role': "user", 'content': query}
        )
        history.append(
            {'role': "system", 'content': response_text}
        )

        await state.update_data(history=history)

    else:
        response_text = f'''ChatGPT вернул ошибку 😞
Код: {response.get('error_code')}
Сообшение: {response.get('error_message')}
Попробуйте ввести другой запрос 😉'''

    text = f'''
<b>Ответ на запрос 💠</b>

<blockquote><pre>{response_text}</pre></blockquote>

<b>Время генерации ответа:</b> <i>{delta_time} секунд(ы) ⏳</i>
'''
    try:
        await message.edit_text(
            text=text
        )     
    except TelegramBadRequest:
        await message.edit_text(
            text='<i>Ответ получился слишком длинным...</i>'
        )
