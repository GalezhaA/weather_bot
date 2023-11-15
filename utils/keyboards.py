from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/weather')
        ],

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
