import requests
import json
import datetime



def get_date() -> dict:
    data = requests.get('http://nekopara.ru/date').json()
    return data


def get_inf_by_date(day=None, month=None, year=None) -> dict:
    data = requests.get(f'http://nekopara.ru/date?day={day}&month={month}&year={year}').json()
    return data


print(get_inf_by_date(5, 2, 2025))