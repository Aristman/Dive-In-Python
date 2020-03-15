import pprint
import requests
from dateutil.parser import parse
import yandex_weather_api
import json


class YandexWeatherForecast:

    def get(self, city):
        lat, lon = '53.894548', '30.330654'
        API_key = '1539ef79-053b-4013-9bea-4b78ec83fe3d'
        url = f'GET https://api.weather.yandex.ru/v1/informers?'
        data = yandex_weather_api.get(requests, api_key=API_key, rate='informers', lat=lat, lon=lon)
        forecast_data = data['forecast']
        forecast = []
        pprint.pprint(json.dumps(forecast_data, indent=4))
        for date_forecast in forecast_data:
            forecast.append({
                'date': date_forecast['date'],
                'temp': date_forecast['parts']['night']['temp_avg']
            })
        return forecast


class CityInfo:

    def __init__(self, city):
        self.city = city
        self._forecast = YandexWeatherForecast()

    def weather_forecast(self):
        return self._forecast.get(self.city)


def _main():
    city_info = CityInfo('Mogilev')
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast)


if __name__ == '__main__':
    _main()
