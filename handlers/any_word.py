from aiogram import Router, F
from aiogram.types import Message
from utils.keyboards import main_kb
router = Router()


@router.message(F.text)
async def any_word(message: Message):
    await message.answer(
        text='Я вас не понимаю.\nВыберите доступную команду из списка.',
        reply_markup=main_kb
    )
