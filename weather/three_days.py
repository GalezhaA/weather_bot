"""
Запрос информации о прогнозе погоды на 3 дня по API
"""

from pprint import pprint

import requests
import config


def get_weather_three_days(city):
    """
    Получает название города, делает request запрос, возвращает информацию о погоде.
    :param city: str
    :return: str
    """
    try:
        querystring = {"q": city, "days": "3", "lang": "ru"}
        response = requests.get(
            url=config.weather_three_days_url,
            headers=config.weather_three_days_headers,
            params=querystring
        )
        data = response.json()
        # pprint(data)

        country = data['location']['country']
        city_name = data['location']['name']
        date_one = data['forecast']['forecastday'][0]['date']
        temperature_one = data['forecast']['forecastday'][0]['day']['avgtemp_c']
        frase_one = data['forecast']['forecastday'][0]['day']['condition']['text']
        # picture_one = data['forecast']['forecastday'][0]['day']['condition']['icon']

        date_two = data['forecast']['forecastday'][1]['date']
        temperature_two = data['forecast']['forecastday'][1]['day']['avgtemp_c']
        frase_two = data['forecast']['forecastday'][1]['day']['condition']['text']

        date_three = data['forecast']['forecastday'][2]['date']
        temperature_three = data['forecast']['forecastday'][2]['day']['avgtemp_c']
        frase_three = data['forecast']['forecastday'][2]['day']['condition']['text']


        return (f'*_*_*_*_*_*_*_*_*_*_*_*_*\n'
                f'Общая информация о погоде в городе {city_name}\n'
                f'Страна: {country}\n\n'
                f'Дата: {date_one}\n'
                f'Температура: {temperature_one}\n'
                f'{frase_one}\n\n'
                f'Дата: {date_two}\n'
                f'Температура: {temperature_two}\n'
                f'{frase_two}\n\n'
                f'Дата: {date_three}\n'
                f'Температура: {temperature_three}\n'
                f'{frase_three}\n'
                f'*_*_*_*_*_*_*_*_*_*_*_*_*\n\n')

    except Exception:
        return 'Проверьте название города'


def main():
    city = input('Введите город: ')
    print(get_weather_three_days(city)[1])


if __name__ == '__main__':
    main()
