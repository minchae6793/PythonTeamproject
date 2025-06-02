import datetime

def get_latest_weekday():
    today = datetime.date.today()
    if today.weekday() == 5:  # 토요일
        search_date = today - datetime.timedelta(days=1)
    elif today.weekday() == 6:  # 일요일
        search_date = today - datetime.timedelta(days=2)
    else:
        search_date = today
    return search_date.strftime('%Y%m%d')
