"""
Стэйты
"""

from aiogram.fsm.state import StatesGroup, State


class WeatherState(StatesGroup):
    city_question = State()


class WeatherThreeState(StatesGroup):
    city_question = State()


class WeatherHistoryState(StatesGroup):
    city_question = State()
