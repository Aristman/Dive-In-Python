import pprint
from Yandex_API import y_weather


def _main():
    my_weather = y_weather.WeatherToSite()
    print(my_weather.get_condition('clear'))
#    forecast = my_weather.get_forecast('53.894548', '30.330654', '97c42aba-7868-4110-9f24-135609aaf07d')
#    with open('farecast.txt', 'w') as f:
#        f.writelines(forecast)
#    pprint.pprint(forecast)


if __name__ == '__main__':
    _main()
