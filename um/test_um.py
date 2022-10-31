from um import count

def test_countSimple():
    assert count('um um') == 2
    assert count('hello um, um.') == 2
    assert count('hello um, um the food is yummy.') == 2

def test_countA():
    assert count('yummy') == 0
    assert count('hello World') == 0
    assert count('Umbrella') == 0
    assert count('Um? Mum? Whats up? Hmm. Um Mum.') == 2

def test_countCase():
    assert count('UM um') == 2
    assert count('UMMMM ummmmm UM um') == 2
    assert count('UM') == 1