import requests
import sys

url = 'http:/github.com/ggjr'
try:
    res = requests.get(url, timeout=30)
    res. raise_for_status()
except requests.Timeout:
    print('Ошибка TIME OUT :', url)
except requests.HTTPError as err:
    print(f'Ошибка url:{url}, code {err.response.status_code}')
except requests.RequestException:
    print('Общая ошибка запроса url:', url)
else:
    print(res.content)