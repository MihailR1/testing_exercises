import datetime

from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_for_tommorow():
    date: str = 'tomorrow'
    time: str = '10:15'
    target_date = datetime.datetime.now() + datetime.timedelta(days=1)
    target_date_and_time = datetime.datetime(target_date.year, target_date.month, target_date.day, 10, 15)
    assert compose_datetime_from(date, time) == target_date_and_time


def test_compose_datetime_for_today():
    date: str = 'today'
    time: str = '10:15'
    target_date = datetime.datetime.now()
    target_date_and_time = datetime.datetime(target_date.year, target_date.month, target_date.day, 10, 15)
    assert compose_datetime_from(date, time) == target_date_and_time
