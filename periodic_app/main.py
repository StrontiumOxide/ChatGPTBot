from apscheduler.schedulers.asyncio import AsyncIOScheduler
from periodic_app.clearing_request_limit import cleaner
from periodic_app.spam import spamer


async def planned_machine(**kwargs) -> None:
    """Функция по установке условий для периодических приложений"""

        # Инициализация класса
    scheduler = AsyncIOScheduler()

    scheduler.add_job(cleaner, 'interval', seconds=60)
    scheduler.add_job(spamer, 'cron', hour=8, minute=0, args=[kwargs.get('bot'), 'morning'])
    scheduler.add_job(spamer, 'cron', hour=22, minute=0, args=[kwargs.get('bot'), 'night'])

    scheduler.start()
