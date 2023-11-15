from aiogram.fsm.state import StatesGroup, State


class WeatherState(StatesGroup):
    city_question = State()


