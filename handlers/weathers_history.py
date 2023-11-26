"""
Обработчик команды /weather_history

Отправляет историю погоды за последние 7 дней
"""

from aiogram import Router
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext

from utils.keyboards import main_kb, exit_btn
from utils.states import WeatherHistoryState
from weather.last_seven_days import weather_output_for_user
from databases.weather_db import HistoryDataModel


router = Router()


@router.message(F.text == 'История погоды за последние 7 дней')
async def set_weather_state(message: Message, state: FSMContext):
    """
    Включает новый стейт.
    Отправляет пользователю запрос города
    :param message:
    :param state:
    :return:
    """
    await state.set_state(WeatherHistoryState.city_question)
    await message.answer('Введите название города', reply_markup=exit_btn)


@router.message(WeatherHistoryState.city_question)
async def send_weather(message: Message, state: FSMContext):
    """
    Вызывает функцию для запроса информации по запрошенному городу.
    Отправляет сообщение с данными пользователю.
    Очищает стейт.
    :param message:
    :param state:
    :return:
    """
    weather_history = weather_output_for_user(message.text)
    if message.text != 'Выйти в меню':
        if weather_history != 'Проверьте название города':
            HistoryDataModel.create(
                tg_id=message.from_user.id,
                data=weather_history
            )
            await message.answer(text=weather_history, reply_markup=main_kb)
            await state.clear()
        else:
            await message.answer(text=weather_history, reply_markup=exit_btn)
    else:
        await state.clear()
        await message.answer(text='Главное меню', reply_markup=main_kb)
