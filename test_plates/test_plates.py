from plates import is_valid

def test_firstLetter():
    """Test whether the first letter is alphabetic"""
    assert is_valid("5CDF45") == False
    assert is_valid("442356") == False
    assert is_valid("AAB20") == True

def test_secondletter():
    """Test whether the second letter is alphabetic"""
    assert is_valid("A2300") == False
    assert is_valid("AAB20") == True

def test_numeric():
    """Test whether the numbers are in between"""
    assert is_valid("AA2B00") == False
    assert is_valid("MM349") == True

def test_length():
    """Test whether the length is less or equal to 6"""
    assert is_valid("AABH456") == False

def test_alphanumeric():
    """test whether it allows non-alphanumeric characters"""
    assert is_valid("AAB@45") == False

def test_zero():
    """the first number cannot be zero"""
    assert is_valid("AABH04") == False