import requests


class WeatherToSite():

    _CONDITION = {
        'clear': 'ясно',
        'partly-cloudy': 'малооблачно',
        'cloudy': 'облачно с прояснениями',
        'overcast': 'пасмурно',
        'partly-cloudy-and-light-rain': 'небольшой дождь',
        'partly-cloudy-and-rain': "дождь",
        'overcast-and-rain': 'сильный дождь',
        'overcast-thunderstorms-with-rain': 'сильный дождь, гроза',
        'cloudy-and-light-rain': 'небольшой дождь',
        'overcast-and-light-rain': 'небольшой дождь',
        'cloudy-and-rain': 'дождь',
        'overcast-and-wet-snow': 'дождь со снегом',
        'partly-cloudy-and-light-snow': 'небольшой снег',
        'partly-cloudy-and-snow': 'снег',
        'overcast-and-snow': 'снегопад',
        'cloudy-and-light-snow': 'небольшой снег',
        'overcast-and-light-snow': 'небольшой снег',
        'cloudy-and-snow': 'снег'
    }

    def get_condition(self, name: str) -> str:
        """Возвращает русское название погоды.

        name - возвращаемое в запросе назавние по-английски"""
        return self._CONDITION[name]

    def __init__(self):
        pass

    def get_forecast(self, lat, lon, API_key, lang='ru_RU'):
        """Метод возвращает прогноз погоды в формаие JSON на ближайшие два периода

        Входные параметры:

        lat, lon - широта и долгота места для прогноза

        API_key - ключ API для сервиса погоды Яндекс

        lang - язык прогноза (см. справке Yandex)
        """
        url = f'https://api.weather.yandex.ru/v1/informers?'
        head = {'X-Yandex-API-Key': API_key}
        params = [
            ('lat', lat),
            ('lon', lon),
            ('lang', lang)
        ]
        return requests.get(url, params=params, headers=head).json()
