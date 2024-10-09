import requests


def get_weather_data(city, api_key):
    # URL для запроса к API OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    # Выполнение запроса
    response = requests.get(url)

    # Проверка, успешен ли запрос
    if response.status_code == 200:
        data = response.json()

        # Извлечение необходимых данных
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


# Замените 'YOUR_API_KEY' на ваш ключ
api_key = '8f27a4758ef564cfad2f354552ccb3da'
city = "Лондон"
get_weather_data(city, api_key)
