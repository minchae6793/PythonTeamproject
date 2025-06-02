import datetime

def get_latest_workday():
    today = datetime.date.today()
    if today.weekday() == 5:  # 토요일
        return today - datetime.timedelta(days=1)
    elif today.weekday() == 6:  # 일요일
        return today - datetime.timedelta(days=2)
    else:
        return today
