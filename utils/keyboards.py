from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)
from weather.three_days import get_weather_three_days


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            # KeyboardButton(text='/weather'),
            KeyboardButton(text='/weather3')
        ],
        [
            KeyboardButton(text='/history')
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие из меню'
)

exit_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/exit')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
#
# three_days_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text=get_weather_three_days(message.text)[1]['date'])
#         ]
#     ]
# )
