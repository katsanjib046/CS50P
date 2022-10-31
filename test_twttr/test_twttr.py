# import the function
from twttr import shorten

def test_lower():
    """ Tests the lower case input """
    assert shorten("hello") == "hll"
    assert shorten("okay") == "ky"

def test_upper():
    """ Tests the upper case input """
    assert shorten("HELLO") == "HLL"
    assert shorten("OKAY") == "KY"

def test_mixed():
    """Tests the mixed case"""
    assert shorten("Hello") == "Hll"
    assert shorten("Okay") == "ky"

def test_anything():
    """Tests when the input has number and everything"""
    assert shorten("Hello123") == "Hll123"
    assert shorten("Eleph@nt") == "lph@nt"
    assert shorten("Hello Bro!") == "Hll Br!"