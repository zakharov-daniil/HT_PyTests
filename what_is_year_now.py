import urllib.request
import json
from unittest.mock import patch
import pytest


API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


def test_exception():
    exp_except = {'currentDateTime': '2020_11_29'}

    with open('exp_except.json', 'w') as exp_except_js:
        json.dump(exp_except, exp_except_js)

    with pytest.raises(ValueError), open('exp_except.json', 'r') as exp_except_js, \
            patch.object(urllib.request, 'urlopen', return_value = exp_except_js):
        what_is_year_now()

@pytest.mark.parametrize('test_date, exp_year', [
    ({'currentDateTime': '2020-11-29'}, 2020),
    ({'currentDateTime': '29.11.2019'}, 2019)
])
def test_get_year(test_date, exp_year):
    with open('date.json', 'w') as date_js:
        json.dump(test_date, date_js)

    with open('date.json', 'r') as date_js, patch.object(urllib.request, 'urlopen', return_value = date_js):
        result_year = what_is_year_now()

    assert result_year == exp_year
