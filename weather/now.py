"""
Запрос информации о погоде в данный момент по API
"""

from pprint import pprint

import requests
import config


def get_weather(city, open_weather_token):
    """
    Делает request запрос, получает информацию, преобразовывает в читаемый для пользователя вид.
    :param city: str
    :param open_weather_token: str
    :return: str
    """
    code_to_smile = {
        'Clear': 'Ясно \U0001F31E',
        'Clouds': 'Облачно \U0001F4A8',
        'Rain': 'Дождь \U0001F4A6',
        'Drizzle': 'Дождь \U0001F4A6',
        'Thunderstorm': 'Гроза \U0001F329',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B'
    }

    try:
        r = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&lang=ru&units=metric'.format(
                city_name=city, API_key=open_weather_token
            )
        )
        data = r.json()
        # pprint(data)

        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = (data['main']['pressure'] * 0.75)
        wind_speed = data['wind']['speed']
        weather_feel = data['weather'][0]['main']
        if weather_feel in code_to_smile:
            wd = code_to_smile[weather_feel]
        else:
            wd = 'Посмотри в окно. Не пойму, что там за погода!'
        country = data['sys']['country']

        return (f'Город: {city}\nТемпература: {temperature}C\n'
                f'Влажность: {humidity}%\nДавление: {pressure} мм. рт. ст.\n'
                f'Скорость ветра: {wind_speed} м/с\n{wd}\n'
                f'Страна: {country}')

    except Exception:
        return 'Проверьте название города'


def main():
    city = input('Введите город: ')
    get_weather(city, config.API_KEY)


if __name__ == '__main__':
    main()
