from fuel import gauge, convert
import pytest

def test_gauge():
    """Tests the gauge functions"""
    assert gauge(20) == "20%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_convert():
    """Tests the convert functions"""
    assert convert("3/4") == 75
    assert convert("1/2") == 50

def test_value_err():
    with pytest.raises(ValueError):
        convert("dog/cat")

def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")