from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.keyboards import main_kb, exit_btn
from utils.states import WeatherState
from weather.now import get_weather
from config import API_KEY


router = Router()


@router.message(Command('weather'))
async def set_weather_state(message: Message, state: FSMContext):
    await state.set_state(WeatherState.city_question)
    await message.answer('Введите название города', reply_markup=exit_btn)


@router.message(WeatherState.city_question)
async def weather_output(message: Message, state: FSMContext):
    weather_now = get_weather(message.text, API_KEY)
    if weather_now != 'Проверьте название города':
        await state.clear()
        await message.answer(weather_now, reply_markup=main_kb)
    else:
        await message.answer(weather_now)
