from aiogram import Router, types as tp
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from main_logic_bot.greetings import kb_greetings as kb
from data.loader_file import load_file

router = Router(name='message_greetings')


@router.message(CommandStart())
async def start_handler(message: tp.Message, state: FSMContext) -> None:
    """Функция по обработке команды /start"""

    await state.clear()
    
    text = f'''
Привет, <b>{message.from_user.full_name}</b> 👋

<blockquote>ChatGPTBot — это инновационный Telegram-бот, который интегрирует возможности ChatGPT прямо в ваш мессенджер! 🤖💬

Теперь вы можете получать быстрые и умные ответы на любые вопросы, общаться на разные темы и использовать функционал искусственного интеллекта прямо из чата! 🗨️ 

Это делает ваши беседы более увлекательными и интерактивными ✨</blockquote>

Для начала общения со мной введите команду <b>/start_conversation</b>
'''

    await message.answer(
        text=text,
        reply_markup=kb.inline.start_link
    )
