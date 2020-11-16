import time
from datetime import datetime


def datetime_to_timestamp(dt):
    t = time.strptime(dt.strftime("%Y-%m-%d"), "%Y-%m-%d")
    return int(time.mktime(t) * 1000)


def today_timestamp():
    return datetime_to_timestamp(datetime.now().date())