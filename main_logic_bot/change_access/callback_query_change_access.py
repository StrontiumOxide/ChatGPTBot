from aiogram import Router, types as tp, F
from aiogram.fsm.context import FSMContext
from utils.states import ChanheAsseccState, ChanheAsseccState_v2
from utils.config import gpt_access
from main_logic_bot.change_access import kb_change_access as kb

router = Router(name='callback_query_change_access')


async def check_text(message: tp.Message) -> bool | None:
    """Функция по проверке наличия текста в сообщении"""

    if not message.text:
        await message.answer(text='Извините, в вашем сообщении нет текста 😒')
        return True
    

@router.callback_query(F.data == 'add_user')
async def change_access_handler(callback: tp.CallbackQuery, state: FSMContext) -> None:
    """Функция по обработке callback_data = add_user"""

    await callback.answer()
    await callback.message.answer(
        text='Напишите имя пользователя 👤'
    )

    await state.set_state(ChanheAsseccState.name)


@router.message(ChanheAsseccState.name)
async def get_name(message: tp.Message, state: FSMContext) -> None:
    """Функция по получению имени пользователя"""

        # Проверка наличия текста в сообщении
    if await check_text(message=message): return

    await state.update_data(name=message.text)

    await message.answer(
        text='Напишите id пользователя 🆔'
    )

    await state.set_state(ChanheAsseccState.user_id)


@router.message(ChanheAsseccState.user_id)
async def get_user_id(message: tp.Message, state: FSMContext) -> None:
    """Функция по получению id пользователя"""

        # Проверка наличия текста в сообщении
    if await check_text(message=message): return

    data: dict = await state.get_data()
    name = data.get('name')

    try:
        user_id = int(message.text)
    except ValueError:  
        await message.answer(
            text='Невозможно перевести в цифру!'
        )
        return
    
    gpt_access[user_id] = name

    await message.answer(
        text='Пользователь добавлен ✅'
    )

    await state.clear()


@router.callback_query(F.data == 'remove_user')
async def change_access_handler(callback: tp.CallbackQuery, state: FSMContext) -> None:
    """Функция по обработке callback_data = remove_user"""

    if not gpt_access:
        await callback.answer(
            text='Ни у кого нет доступа к ChatGPT 🚫',
            show_alert=True
        )
        return
    
    await callback.answer()
    await callback.message.answer(
        text='Кому ограничить доступ❓',
        reply_markup=kb.reply.created_kb_user()
    )

    await state.set_state(ChanheAsseccState_v2.name)


@router.message(ChanheAsseccState_v2.name)
async def get_user_delete(message: tp.Message, state: FSMContext) -> None:
    """Функция по получении информации о пользователе для удаления"""

    try:
        name, user_id = message.text.split(sep=' - ')
    except ValueError:
        await message.answer(
            text='Ошибка ввода 🚫'
        )
        return
    
    if int(user_id) in gpt_access:
        del gpt_access[int(user_id)]
        await state.clear()
        text = f'Вы ограничили пользователю <b>"{name}"</b> доступ к ChatGPT!'
    else:
        text = 'Такого пользователя нет 🚫'

    await message.answer(
            text=text,
            reply_markup=kb.reply.remove
        )
