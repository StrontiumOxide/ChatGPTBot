from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update, Message
from utils.config import active_people, gpt_active


class CountMiddleware(BaseMiddleware):
    """Middleware по счёту апдейтов"""

    async def __call__(self, handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]], event: Update, data: Dict[str, Any]) -> Any:
        
        if event.message:
            user_id = event.message.from_user.id
        elif event.callback_query:
            user_id = event.callback_query.from_user.id
        else:
            return

        if user_id in active_people:
            active_people[user_id]['count'] += 1
        else:
            active_people[user_id] = {'count': 1, 'status': True}

            # Выполнение соответствующего хендлера
        if active_people[user_id]['count'] > 50:
            if active_people[user_id]['status']:
                active_people[user_id]['status'] = False
                text = f'''
⚠️ <b>ВНИМАНИЕ</b> ⚠️

<b>от API Telegram</b>
<blockquote>Уважаемый, <b>{event.message.from_user.full_name}</b>❗️
Вы превысили лимит по запросам 💭
Повторите пожалуйста позже ⏳
</blockquote>
'''
                await event.message.answer(
                    text=text
                )
            return
        
        await handler(event, data)

        return await super().__call__(handler, event, data)
    

class CheckActiveMiddleware(BaseMiddleware):
    """Middleware по контролю запросов к ChatGPT"""

    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], message: Message, data: Dict[str, Any]) -> Any:
        
        user_id = message.from_user.id

        if user_id in gpt_active:
            await message.reply(
                text='<b>Подождите❗️</b>\n<i>ChatGPT ещё обрабатывает предыдущий запрос...</i>'
            )
        else:
            await handler(message, data)
        
        return await super().__call__(handler, message, data)
    