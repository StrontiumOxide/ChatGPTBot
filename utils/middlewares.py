from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Update
from utils.config import active_people


class CountMiddleware(BaseMiddleware):
    """Middleware по счёту апдейтов"""

    async def __call__(self, handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]], event: Update, data: Dict[str, Any]) -> Any:
        
        if event.message:
            user_id = event.message.from_user.id

        elif event.callback_query:
            user_id = event.callback_query.from_user.id

        if user_id in active_people:
            active_people[user_id]['count'] += 1
        else:
            active_people[user_id] = {'count': 1}

            # Выполнение соответствующего хендлера
        await handler(event, data)

        return await super().__call__(handler, event, data)
    

class CheckActiveMiddleware(BaseMiddleware):
    """Middleware по контролю запросов к ChatGPT"""
    