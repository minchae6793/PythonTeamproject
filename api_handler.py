import requests
import certifi
from utils import get_latest_weekday

API_KEY = 'IxEHH68rtEBltFGI0LNjGieE4AdYKE9f'
URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

def fetch_exchange_data():
    params = {
        'authkey': API_KEY,
        'searchdate': get_latest_weekday(),
        'data': 'AP01'
    }
    response = requests.get(URL, params=params, verify=certifi.where())
    if response.status_code == 200:
        return response.json()
    else:
        raise ConnectionError("API 요청 실패 (status code: {})".format(response.status_code))
