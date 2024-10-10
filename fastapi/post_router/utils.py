import logging

import requests


def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            data = response.json()

            town = data['name']
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            weather_description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            weather_dict = {
                "town": town,
                "temperature": temperature,
                "feels_like": feels_like,
                "weather_description": weather_description,
                "humidity": humidity,
                "wind_speed": wind_speed

            }
            return weather_dict
        else:
            return None
    except requests.exceptions.RequestException as e:
        logging.warning(e)
        return None
