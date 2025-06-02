def find_currency_rate(data, currency_code):
    return next((item for item in data if item["cur_unit"] == currency_code), None)

def calculate(amount, rate, direction):
    if direction == '1':  # 원화 -> 외화
        return round(amount / rate, 2)
    elif direction == '2':  # 외화 -> 원화
        return round(amount * rate, 0)
    else:
        raise ValueError("잘못된 변환 방향입니다 (1 또는 2만 허용).")
