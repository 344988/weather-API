import requests
import time

class WeatherSDK:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.cache = {}  # Для кэширования результатов

    def get_weather(self, city_name):
        # Проверка кэша
        if city_name in self.cache:
            # Возвращаем кэшированные данные, если они еще актуальны
            cached_data, timestamp = self.cache[city_name]
            if (time.time() - timestamp) < 600:  # 10 минут в секундах
                return cached_data

        try:
            params = {'q': city_name, 'appid': self.api_key, 'units': 'metric'}
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            weather_data = response.json()
            # Обновление кэша
            self.cache[city_name] = (weather_data, time.time())
            return weather_data
        except requests.ConnectionError:
            return {"error": "Ошибка подключения к сети"}
        except requests.Timeout:
            return {"error": "Превышено время ожидания запроса"}
        except requests.HTTPError as http_err:
            return {"error": f"HTTP ошибка: {http_err}"}
        except requests.RequestException as req_err:
            return {"error": f"Ошибка запроса: {req_err}"}

# Пример использования SDK
api_key = "your_api_key_here"  # Замените на ваш API-ключ
sdk = WeatherSDK(api_key)
weather_data = sdk.get_weather("Moscow")
print(weather_data)
