from aiogram import Router, types as tp
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from main_logic_bot.change_access import kb_change_access as kb

router = Router(name='message_change_access')


@router.message(Command(commands=['change_access']))
async def change_access_handler(message: tp.Message, state: FSMContext) -> None:
    """Функция по обработке команды /change_access"""

    await state.clear()

    text = '''
<b>Секретное меню</b>
Выберите действие ⬇️
'''

    await message.answer(
        text=text,
        reply_markup=kb.inline.kb_change
    )
