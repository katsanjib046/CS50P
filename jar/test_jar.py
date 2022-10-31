from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(10)
    assert jar.capacity == 10

def test_errors():
    with pytest.raises(ValueError):
        jar = Jar(-5)
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(20)
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(2)
        jar.withdraw(5)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5

def test_capacity():
    jar = Jar()
    assert jar.capacity == 12
    jar.capacity = 10
    assert jar.capacity == 10

def test_size():
    jar = Jar()
    assert jar.size == 0
    jar.size = 5
    assert jar.size == 5