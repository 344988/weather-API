import sys
import unittest
from unittest.mock import patch
from datetime import datetime, timedelta

# Добавляем путь к каталогу, содержащему модуль weather_sdk
sys.path.append('../src')

# Теперь мы можем импортировать класс WeatherSDK из модуля weather_sdk
from weather_sdk import WeatherSDK

class TestWeatherSDK(unittest.TestCase):

    def setUp(self):
        self.api_key = 'fake_api_key'
        self.sdk = WeatherSDK(self.api_key)

    @patch('weather_sdk.requests.get')
    def test_get_weather_valid_city(self, mock_get):
        # Здесь мы создаем фиктивный ответ от requests.get, как если бы он пришел от OpenWeatherMap
        mock_get.return_value.json.return_value = {
            "weather": [{"main": "Clear", "description": "clear sky"}],
            "main": {"temp": 15.0},
            "name": "London",
            "cod": 200
        }

        # Вызываем функцию, как если бы мы делали реальный запрос к API
        result = self.sdk.get_weather("London")
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], "London")
        self.assertEqual(result['weather'][0]['main'], "Clear")
        self.assertEqual(result['main']['temp'], 15.0)

    @patch('weather_sdk.requests.get')
    def test_get_weather_invalid_city(self, mock_get):
        # Фиктивный ответ для несуществующего города
        mock_get.return_value.json.return_value = {
            "cod": "404",
            "message": "city not found"
        }

        result = self.sdk.get_weather("InvalidCity")
        self.assertIsNotNone(result)
        self.assertIn("cod", result)
        self.assertEqual(result["cod"], "404")

    # Тут можно добавить дополнительные тесты, например, для проверки кэширования
    def test_caching(self):
        # Прописываем логику для тестирования механизма кэширования в SDK
        pass

if __name__ == '__main__':
    unittest.main()

