from aiogram import Router, types as tp
from aiogram.filters import CommandStart
from main_logic_bot.greetings import kb_greetings as kb
from data.loader_file import load_file

router = Router(name='message_greetings')


@router.message(CommandStart())
async def start_handler(message: tp.Message) -> None:
    """Функция по обработке команды /start"""

    text = f'''
Привет, <b>{message.from_user.full_name}</b> 👋

<blockquote>ChatGPTBot — это инновационный Telegram-бот, который интегрирует возможности ChatGPT прямо в ваш мессенджер! 🤖💬

Теперь вы можете получать быстрые и умные ответы на любые вопросы, общаться на разные темы и использовать функционал искусственного интеллекта прямо из чата! 🗨️✨ Это делает ваши беседы более увлекательными и интерактивными.

Вы можете легко задавать вопросы, получать советы, генерировать идеи и даже просто развлекаться. 🎉💡 С ChatGPTBot ваш повседневный чат станет более интересным и информативным! Не упустите возможность взаимодействовать с передовыми технологиями прямо в Telegram! 🚀📱

Присоединяйтесь к общению с ChatGPTBot и откройте для себя мир возможностей! 🌍💖</blockquote>

Для начала общения со мной введите команду <b>/start_conversation</b>
'''

    await message.answer_photo(
        photo=load_file(category='photo', filename='avatar.png'),
        caption=text,
        reply_markup=kb.inline.start_link
    )
