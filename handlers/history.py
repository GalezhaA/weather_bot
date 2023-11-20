from databases.weather_db import User
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from utils.keyboards import main_kb

router = Router()


@router.message(Command('history'))
async def history(message: Message):
    info = ''.join(User.find_user(message.from_user.id))
    await message.answer(text=info, reply_markup=main_kb)