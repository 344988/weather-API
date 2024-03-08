# MyWeatherSDK

## Описание
MyWeatherSDK - это небольшая библиотека на Python, предоставляющая удобный доступ к данным о погоде через OpenWeatherMap API. Это SDK позволяет пользователям легко запрашивать текущие погодные условия для различных городов.

## Установка

Прежде всего, убедитесь, что у вас установлен Python 3. Чтобы установить MyWeatherSDK, следуйте следующим шагам:

1. Клонируйте репозиторий:
    git clone https://your-repository-url.git
    cd your-repository-folder

2. (Опционально) Создайте и активируйте виртуальное окружение:
    python -m venv venv
    source venv/bin/activate # На Unix или MacOS
    venv\Scripts\activate # На Windows

3. Установите зависимости:
    pip install -r requirements.txt


  ## Конфигурация

Чтобы использовать MyWeatherSDK, вам необходимо получить API ключ от OpenWeatherMap:

1. Перейдите на сайт [OpenWeatherMap](https://openweathermap.org/) и зарегистрируйтесь.

2. После регистрации перейдите в свой личный кабинет и скопируйте ваш API ключ.

3. Вставьте этот ключ в соответствующее место в коде SDK или используйте его как переменную среды.

## Пример использования

```python
from weather_sdk import WeatherSDK

# Инициализация SDK с вашим API-ключом
api_key = "your_api_key_here"
sdk = WeatherSDK(api_key)

# Запрос погоды для Москвы
weather_data = sdk.get_weather("Moscow")
print(weather_data)

Тестирование
Для запуска юнит-тестов используйте следующую команду:


python -m unittest
Лицензия
Укажите здесь информацию о лицензии, если таковая имеется.




Убедитесь, что вы замените `https://your-repository-url.git` и `your-repository-folder` на соответствующие URL и название вашего репозитория. Важно также обеспечить наличие файла `requirements.txt` с перечнем необходимых для установки зависимостей.
