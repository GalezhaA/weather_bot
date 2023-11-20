from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from databases.weather_db import User
from utils.keyboards import main_kb, exit_btn
from utils.states import WeatherThreeState
from weather.three_days import get_weather_three_days


router = Router()


@router.message(Command('weather3'))
async def set_weather_state(message: Message, state: FSMContext):
    await state.set_state(WeatherThreeState.city_question)
    await message.answer('Введите название города', reply_markup=exit_btn)


@router.message(WeatherThreeState.city_question)
async def weather_output(message: Message, state: FSMContext):

    weather_three_days_for_message = get_weather_three_days(message.text)
    if weather_three_days_for_message != 'Проверьте название города':
        User.create(
            tg_id=message.from_user.id,
            first_name=message.from_user.username,
            data=weather_three_days_for_message
        )
        await state.clear()
        await message.answer(text=weather_three_days_for_message, reply_markup=main_kb)
    else:
        await message.answer(weather_three_days_for_message)
