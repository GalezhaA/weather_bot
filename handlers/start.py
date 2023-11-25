"""
Обработчик команды /start

Отправляет приветственное сообщение
"""

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from utils.keyboards import main_kb

router = Router()


@router.message(Command('start'))
async def start_func(message: Message):
    """
    Отправляет приветственное сообщение
    :param message: Message
    :return: None
    """
    await message.answer(text=f'Привет, {message.from_user.first_name}!\U0001f607\U0001F917',
                         reply_markup=main_kb)
    await message.answer(text='Чтобы узнать подробнее о командах, нажми на /help')
