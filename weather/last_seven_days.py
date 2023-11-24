"""
Функции для запроса к API weatherapi-com.p.rapidapi.com
Информацию о погоде за последние 7 дней в выбранном городе
"""
import config
import datetime
from datetime import timedelta

import requests


def weather_history_seven_days(city: str) -> dict|str:
    """
    Делает реквест запрос к weatherapi-com.p.rapidapi.com
    Проверяет название города на корректность.
    Возвращает словарь с данными либо сообщение об ошибке.
    :param city:
    :return:
    """
    today = datetime.date.today()
    date = today - timedelta(days=7)
    querystring = {"q": f"{city}", "dt": date, "lang": "ru", "end_dt": today}
    response = requests.get(
        config.history_seven_days_url,
        headers=config.history_seven_days_headers,
        params=querystring
    )
    if list(response.json().keys())[0] == 'error':
        return 'Проверьте название города'
    else:
        return response.json()


def weather_output(city: str) -> dict|str:
    """
    Отбирает из запроса нужные данные.
    Возвращает словарь с данными либо сообщение об ошибке.
    :param city: str
    :return: dict|str
    """
    data = weather_history_seven_days(city)
    if data != 'Проверьте название города':
        history_seven_days = {}
        for num in range(7):
            main_info = [data['forecast']['forecastday'][num]['date'],
                         str(data['forecast']['forecastday'][num]['day']['avgtemp_c']),
                         data['forecast']['forecastday'][num]['day']['condition']['text']]
            history_seven_days[num] = main_info
        return history_seven_days
    else:
        return 'Проверьте название города'


def weather_output_for_user(city: str) -> str:
    """
    Возвращает отформатированный текс для отправки юзеру
    :param city:
    :return:
    """
    data = weather_output(city)
    if data != 'Проверьте название города':
        message = (f'История последних семи дней в городе {city}:\n\n'
                   f'Дата: {data[0][0]}\n'
                   f'Температура: {data[0][1]}\n'
                   f'{data[0][2]}\n\n'
                   f'Дата: {data[1][0]}\n'
                   f'Температура: {data[1][1]}\n'
                   f'{data[1][2]}\n\n'
                   f'Дата: {data[2][0]}\n'
                   f'Температура: {data[2][1]}\n'
                   f'{data[2][2]}\n\n'
                   f'Дата: {data[3][0]}\n'
                   f'Температура: {data[3][1]}\n'
                   f'{data[3][2]}\n\n'
                   f'Дата: {data[4][0]}\n'
                   f'Температура: {data[4][1]}\n'
                   f'{data[4][2]}\n\n'
                   f'Дата: {data[5][0]}\n'
                   f'Температура: {data[5][1]}\n'
                   f'{data[5][2]}\n\n'
                   f'Дата: {data[6][0]}\n'
                   f'Температура: {data[6][1]}\n'
                   f'{data[6][2]}\n\n'
                   )
        return message
    else:
        return 'Проверьте название города'


