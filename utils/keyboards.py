"""
Подключаемые клавиатуры
"""

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)
from weather.three_days import get_weather_three_days


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Погода сейчас'),
            KeyboardButton(text='Прогноз погоды на 3 дня')
        ],
        [
            KeyboardButton(text='История погоды за последние 7 дней'),
            KeyboardButton(text='История запросов')
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие из меню'
)

exit_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Выйти в меню', )
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


