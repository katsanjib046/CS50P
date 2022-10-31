from numb3rs import validate


def test_numb3rs1():
    assert validate("1.0.1.1") == True
    assert validate("123.123.2.0") == True
    assert validate("456.1.2.6") == False
    assert validate("1.23.45.4456") == False
    assert validate("1.0.259.1") == False

def test_numb3rs2():
    assert validate("1.0.1.1.1") == False
    assert validate("cat") == False
    assert validate("cat.dog.a.b") == False
    assert validate("0.00.00.1") == True