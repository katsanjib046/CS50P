from working import convert
import pytest


def test_convertNormal():
    assert convert('9:00 AM to 5:30 PM') == '09:00 to 17:30'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 PM to 5:30 AM') == '21:00 to 05:30'
    assert convert('9:30 AM to 5:30 AM') == '09:30 to 05:30'
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'


def test_convertError():
    with pytest.raises(ValueError):
        convert('9AM to 5PM')
    with pytest.raises(ValueError):
        convert('9AM 5PM')
    with pytest.raises(ValueError):
        convert('9 AM to 17 PM')
    with pytest.raises(ValueError):
        convert('13:00 PM to 18:00 PM')

def test_convertInvalid():
    with pytest.raises(ValueError):
        convert('11:60 AM to 5:00 PM')
    with pytest.raises(ValueError):
        convert('11:60 AM to 5:00 PM')

