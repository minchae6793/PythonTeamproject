import requests

def fetch_exchange_rates(api_key, search_date_str):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey': api_key,
        'searchdate': search_date_str,
        'data': 'AP01'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None