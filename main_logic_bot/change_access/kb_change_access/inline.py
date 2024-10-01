from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_change = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить ✅', callback_data='add_user'),
            InlineKeyboardButton(text='Убрать ❌', callback_data='remove_user')
        ]
    ]
)
