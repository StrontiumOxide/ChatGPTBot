import asyncio

from utils.config import active_people

sleeping = 120


async def cleaning() -> None:
    """Функция по периодической чистке актива"""

    while True:
        await asyncio.sleep(sleeping)
        active_people.clear()
