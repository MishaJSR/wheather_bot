import requests


def get_weather_data(city, api_key):
    # URL для запроса к API OpenWeatherMap
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}&limit=1"

    # Выполнение запроса
    response = requests.get(url)

    # Проверка, успешен ли запрос
    if response.status_code == 200:
        data = response.json()[0]
        lat, lon = data["lat"], data["lon"]

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        # Извлечение необходимых данных
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Вывод данных
        print(f"Город: {city}")
        print(f"Температура: {temperature}°C")
        print(f"Ощущается как: {feels_like}°C")
        print(f"Описание погоды: {weather_description}")
        print(f"Влажность: {humidity}%")
        print(f"Скорость ветра: {wind_speed} м/с")
    else:
        print(f"Ошибка {response.status_code}: Не удалось получить данные для города {city}")


# Замените 'YOUR_API_KEY' на ваш ключ
api_key = '8f27a4758ef564cfad2f354552ccb3da'
city = "London"
get_weather_data(city, api_key)
