"""
Обработчик команды /history

Выдаёт историю запросов
"""

from databases.weather_db import HistoryDataModel
from aiogram import Router
from aiogram.types import Message
from utils.keyboards import main_kb
from aiogram import F


router = Router()


@router.message(F.text == 'История запросов')
async def history(message: Message):
    """
    Выдаёт историю запросов
    :param message: Message
    :return: None
    """
    await message.answer(text='История последних запросов:')

    info = HistoryDataModel.find_user(message.from_user.id)
    for obj in info:
        await message.answer(text=obj, reply_markup=main_kb)