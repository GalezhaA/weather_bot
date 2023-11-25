"""
Обработчик команды /help
"""

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from utils.keyboards import main_kb

router = Router()

help_message = ('Привет! Это бот для поиска погоды.\n'
                'У меня есть 4 команды:\n\n'
                '"Погода сейчас" - показывает погоду в данный момент времени в любом городе.\n\n'
                '"Прогноз погоды на 3 дня" - прогноз погоды на 3 дня в любом городе (включая сегодняшний день)\n\n'
                '"История погоды за последние 7 дней" - история погоды за последние 7 дней в любом городе (включая '
                'сегодняшний день)\n\n'
                '"История запросов" - история твоих последних запросов (максимум 10)')


@router.message(Command('help'))
async def start_func(message: Message):
    """
    Отправляет пользователю информацию о боте
    :param message: Message
    :return:
    """
    await message.answer(text=help_message, reply_markup=main_kb)
