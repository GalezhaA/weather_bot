"""
Обработчик команды /weather3

Отправляет прогноз погоды на 3 дня в любом городе
"""

from aiogram import Router
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext

from databases.weather_db import HistoryDataModel
from utils.keyboards import main_kb, exit_btn
from utils.states import WeatherThreeState
from weather.three_days import get_weather_three_days


router = Router()


@router.message(F.text == 'Прогноз погоды на 3 дня')
async def set_weather_state(message: Message, state: FSMContext):
    """
        Отправляет пользователю сообщение с запросом города.
        Меняет стэйт
        :param message: Message
        :param state: FSMContext
        :return: None
        """
    await state.set_state(WeatherThreeState.city_question)
    await message.answer('Введите название города', reply_markup=exit_btn)


@router.message(WeatherThreeState.city_question)
async def weather_output(message: Message, state: FSMContext):
    """
    Проверяет, существует ли город, отправляет сообщение с информацией.
    Заносит юзера и информацию в БД.
    Меняет стэйт.
    :param message: Message
    :param state: FSMContext
    :return: None
    """
    weather_three_days_for_message = get_weather_three_days(message.text)
    if message.text != 'Выйти в меню':
        if weather_three_days_for_message != 'Проверьте название города':
            HistoryDataModel.create(
                tg_id=message.from_user.id,
                data=weather_three_days_for_message
            )
            await state.clear()
            await message.answer(text=weather_three_days_for_message, reply_markup=main_kb)
        else:
            await message.answer(weather_three_days_for_message)
    else:
        await state.clear()
        await message.answer(text='Главное меню')