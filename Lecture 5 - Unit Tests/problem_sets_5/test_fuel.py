import math
import pytest
from fuel import convert, gauge

def test_conversion():
    assert convert("2/3") != 1, 2
    assert convert("1/2") != 3, 4


def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_empty_full():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_whole_number():
    assert gauge(2) == "2%"
    assert gauge(33) == "33%"
    assert gauge(34) == "34%"
    assert gauge(50) == "50%"
    assert gauge(66) == "66%"
    assert gauge(67) == "67%"


def test_rounding():
    assert gauge(round(float(33.3))) == "33%"
    assert gauge(round(float(33.7))) == "34%"
    assert gauge(round(float(66.4))) == "66%"
    assert gauge(round(float(66.7))) == "67%"
    assert gauge(round(float(87.3))) == "87%"
    assert gauge(round(float(87.6))) == "88%"
