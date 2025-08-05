# Imports
import pytest
from datetime import date
from seasons import validate_date, convert_days, convert_minutes_to_string


def test_validate_date():
    assert validate_date("1989-09-07", date.today()) == "1989-09-07"
    assert validate_date("1999-01-01", date.today()) == "1999-01-01"

    with pytest.raises(SystemExit) as invalid_date:
        validate_date("2053-08-06", date.today())
    assert invalid_date.type == SystemExit
    assert invalid_date.value.code == "Invalid date format"

    with pytest.raises(SystemExit) as literal_date:
        validate_date("Febuary 6th, 1963", date.today())
    assert literal_date.type == SystemExit
    assert literal_date.value.code == "Invalid date format"


def test_convert_days():
    assert convert_days("13117 days, 0:00:00") == 18888480


def test_convert_minutes_to_string():
    assert convert_minutes_to_string(525600).capitalize() == "Five hundred twenty-five thousand, six hundred minutes"