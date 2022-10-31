from seasons import calculate_minute
from datetime import date
import pytest


def test_calculate_minute():
    assert calculate_minute(date.fromisoformat('2021-08-21')) == 'Five hundred twenty-five thousand, six hundred minutes'
    assert calculate_minute(date.fromisoformat('2020-08-21')) == 'One million, fifty-one thousand, two hundred minutes'

def test_calculate_minute1():
    with pytest.raises(ValueError):
        assert calculate_minute(date.fromisoformat('2021-8-21'))
