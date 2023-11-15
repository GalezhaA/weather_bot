import asyncio, logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import weather, start, help

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(
        weather.router,
        start.router,
        help.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())