"""
Основной файл, запускающий бота.
"""

import asyncio, logging
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from databases.weather_db import db, HistoryDataModel
from handlers import weather_now, start, help,weather_three_days, history, weathers_history, any_word

bot = Bot(BOT_TOKEN)  # Cюда вставлять токен бота
dp = Dispatcher()


async def main():
    """
    Получает роутеры, запускает бота.
    :return: None
    """
    dp.include_routers(
        weather_now.router,
        weather_three_days.router,
        start.router,
        help.router,
        history.router,
        weathers_history.router,
        any_word.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    db.connect(reuse_if_open=True)
    if not HistoryDataModel.table_exists():
        db.create_tables([HistoryDataModel])
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
