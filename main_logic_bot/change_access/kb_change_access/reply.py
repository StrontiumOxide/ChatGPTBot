from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from utils.config import gpt_access

remove = ReplyKeyboardRemove()


def created_kb_user() -> ReplyKeyboardMarkup:
    """Функция по созданию клавиатуры из пользователей"""

    kb = ReplyKeyboardBuilder()
    
    list_btn = [KeyboardButton(text=f'{name} - {u_id}') for u_id, name in gpt_access.items()]

    kb.row(*sorted(list_btn, key=lambda x: x.text), width=1)
    r = kb.as_markup()
    r.resize_keyboard = True
    return r
    