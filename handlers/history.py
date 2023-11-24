"""
Обработчик команды /history

Выдаёт историю запросов
"""

from databases.weather_db import User
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from utils.keyboards import main_kb

router = Router()


@router.message(Command('history'))
async def history(message: Message):
    """
    Выдаёт историю запросов
    :param message: Message
    :return: None
    """
    info1 = ''.join(User.find_user(message.from_user.id))
    print(info1)
    await message.answer(text='История последних запросов:')
    await message.answer(text=info1, reply_markup=main_kb)