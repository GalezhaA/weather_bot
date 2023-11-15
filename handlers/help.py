from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from utils.keyboards import main_kb

router = Router()


@router.message(Command('help'))
async def start_func(message: Message):
    await message.answer(text=f'Введите /weather чтобы узнать погоду', reply_markup=main_kb)
