from utils.config import active_people


async def cleaner() -> None:
    """Функция по очистке кеша запросов от пользователей"""

    active_people.clear()
