from date_util import get_latest_workday
from api import fetch_exchange_rates
from exchange_calculator import calculate_exchange

# 날짜 설정
search_date = get_latest_workday()
search_date_str = search_date.strftime('%Y%m%d')

# API 키
api_key = 'IxEHH68rtEBltFGI0LNjGieE4AdYKE9f'

# 환율 정보 가져오기
data = fetch_exchange_rates(api_key, search_date_str)

if data:
    print("=== 오늘의 환율 정보 ===")
    for item in data:
        print(f"{item['cur_unit']}: {item['deal_bas_r']}원")

    print("\n=== 환율 계산기 ===")
    currency_exchange = input("환전을 원하는 나라의 통화 코드를 입력해주세요.: ").upper()
    direction = input("변환 방향을 선택하세요 (1: 원화 -> 외화, 2: 외화 -> 원화): ").strip()
    money = float(input("환전할 금액을 입력해주세요: "))

    result, error = calculate_exchange(data, currency_exchange, direction, money)
    if error:
        print(error)
    else:
        print(result)
else:
    print("API 요청을 실패하였습니다. 다시 시도해주세요!!")