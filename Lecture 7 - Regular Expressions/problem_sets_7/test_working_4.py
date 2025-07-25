import pytest
from working_4 import time_conversion

def test_am_to_pm():
    assert time_conversion("9 AM TO 9 PM") == "09:00 to 21:00"
    assert time_conversion("7:00 AM TO 3:00 PM") == "07:00 to 15:00"
    assert time_conversion("1:32 AM TO 8:45 PM") == "01:32 to 20:45"

def test_am_to_am():
    assert time_conversion("1 AM TO 11 AM") == "01:00 to 11:00"
    assert time_conversion("3:00 AM TO 8:00 AM") == "03:00 to 08:00"
    assert time_conversion("12:30 AM TO 8:50 AM") == "00:30 to 08:50"

def test_pm_to_am():
    assert time_conversion("9 PM TO 6 AM") == "21:00 to 06:00"
    assert time_conversion("7:00 PM TO 2:00 AM") == "19:00 to 02:00"
    assert time_conversion("8:45 PM TO 5:36 AM") == "20:45 to 05:36"

def test_pm_to_pm():
    assert time_conversion("1 PM TO 9 PM") == "13:00 to 21:00"
    assert time_conversion("2:00 PM TO 11:00 PM") == "14:00 to 23:00"
    assert time_conversion("4:23 PM TO 10:32 PM") == "16:23 to 22:32"

def test_value_error():
    with pytest.raises(ValueError):
        time_conversion()
    with pytest.raises(ValueError):
        time_conversion()
    with pytest.raises(ValueError):
        time_conversion()