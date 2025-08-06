from jar import Jar
import pytest


def test_init():
    jar = Jar()
    with pytest.raises(ValueError) as value_error:
        jar.__init__(-1)
    assert value_error.type == ValueError
    

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1) == "🍪"

def test_deposit():
    ...