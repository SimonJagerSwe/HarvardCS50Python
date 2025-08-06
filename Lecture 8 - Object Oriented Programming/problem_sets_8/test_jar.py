from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar_1 = Jar(3)
    assert jar_1.capacity == 3
    with pytest.raises(ValueError) as value_error:
        jar.__init__(-1)
    assert value_error.type == ValueError
    
    
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(2)
    assert jar.size == 5
    with pytest.raises(ValueError) as value_error:
        jar.deposit(13)
    assert value_error.type == ValueError


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(3)
    assert jar.size == 9
    with pytest.raises(ValueError) as value_error:
        jar.deposit(3)
        jar.withdraw(15)
    assert value_error.type == ValueError