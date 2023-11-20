from pprint import pprint

import requests
import config


def get_weather_three_days(city):
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
        picture_one = data['forecast']['forecastday'][0]['day']['condition']['icon']

        date_two = data['forecast']['forecastday'][1]['date']
        temperature_two = data['forecast']['forecastday'][1]['day']['avgtemp_c']
        frase_two = data['forecast']['forecastday'][1]['day']['condition']['text']
        picture_two = data['forecast']['forecastday'][1]['day']['condition']['icon']

        date_three = data['forecast']['forecastday'][2]['date']
        temperature_three = data['forecast']['forecastday'][2]['day']['avgtemp_c']
        frase_three = data['forecast']['forecastday'][2]['day']['condition']['text']
        picture_three = data['forecast']['forecastday'][2]['day']['condition']['icon']

        first_day = {
            'date': date_one,
            'temperature': temperature_one,
            'frase': frase_one,
            'picture': picture_one
        }

        second_day = {
            'date': date_two,
            'temperature': temperature_two,
            'frase': frase_two,
            'picture': picture_two
        }

        third_day = {
            'date': date_three,
            'temperature': temperature_three,
            'frase': frase_three,
            'picture': picture_three
        }

        return (f'Общая информация о погоде в городе {city_name}\n'
                f'Страна: {country}\n\n'
                f'Дата: {date_one}\n'
                f'Температура: {temperature_one}\n'
                f'{frase_one}\n\n'
                f'Дата: {date_two}\n'
                f'Температура: {temperature_two}\n'
                f'{frase_two}\n\n'
                f'Дата: {date_three}\n'
                f'Температура: {temperature_three}\n'
                f'{frase_three}\n\n')

    except Exception:
        return 'Проверьте название города'


def get_dates(city):
    querystring = {"q": city, "days": "3", "lang": "ru"}
    response = requests.get(
        url=config.weather_three_days_url,
        headers=config.weather_three_days_headers,
        params=querystring
    )
    data = response.json()
    date_one = data['forecast']['forecastday'][0]['date']

    return date_one


def main():
    city = input('Введите город: ')
    print(get_weather_three_days(city)[1])
    print(get_dates(city))


if __name__ == '__main__':
    main()
