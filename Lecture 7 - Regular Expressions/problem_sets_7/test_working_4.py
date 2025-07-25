from working_4 import time_conversion


def test_valid_am_to_am():
    assert time_conversion("1 AM TO 9 AM") == "01:00 to 09:00"
    assert time_conversion("1:32 AM TO 8:45 AM") == "01:32 to 08:45"

def test_valid_pm_to_pm():
    assert time_conversion("12 PM TO 9 PM") == "12:00 to 21:00"
    assert time_conversion("12:01 PM TO 9:32 PM") == "12:01 to 21:32"
    
def test_valid_am_to_pm():
    assert time_conversion("9 AM TO 5 PM") == "09:00 to 17:00"
    assert time_conversion("3:15 AM TO 11:45 PM") == "03:15 to 23:45"

def test_valid_pm_to_am():
    assert time_conversion("2 PM TO 1 AM") == "14:00 to 01:00"
    assert time_conversion("7:34 PM TO 12:34 AM") == "19:34 to 00:34"

def test_valid__12_to_12():
    assert time_conversion("12 AM TO 12 PM") == "00:00 to 12:00"
    assert time_conversion("12 AM TO 12 AM") == "00:00 to 00:00"
    assert time_conversion("12 PM TO 12 AM") == "12:00 to 00:00"
    assert time_conversion("12 PM TO 12 PM") == "12:00 to 12:00"
