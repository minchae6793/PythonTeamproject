def calculate_exchange(data, currency_code, direction, money):
    match = next((item for item in data if item["cur_unit"] == currency_code), None)
    
    if not match:
        return None, "해당 통화 코드를 찾을 수 없습니다."

    rate = float(match["deal_bas_r"].replace(",", ""))
    
    if direction == '1':
        result = money / rate
        return f"{money:,.0f}원 ➝ 약 {result:.2f} {currency_code}", None
    elif direction == '2':
        result = money * rate
        return f"{money:.2f} {currency_code} ➝ 약 {result:,.0f}원", None
    else:
        return None, "올바른 방향을 선택해주세요 (1 또는 2)."