from aiogram import Router, types as tp
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

router = Router(name='message_get_id')


@router.message(Command(commands='get_id'))
async def get_id_handler(message: tp.Message, state: FSMContext) -> None:
    """Функция по обработке команды /start"""

    await state.clear()
    
    await message.answer(
        text=f'Ваш id: <b><code>{message.from_user.id}</code></b>'
    )
