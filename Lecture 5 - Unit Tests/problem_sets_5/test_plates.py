from plates import is_valid


def test_num_start():
    assert is_valid("12") == False

def test_length():
    assert is_valid("NINECHARS") == False
    assert is_valid("A") == False

def test_zero():
    assert is_valid("AB01") == False
    assert is_valid("AB10") == True

def test_mid_num():
    assert is_valid("AB12CD") == False
    assert is_valid("A1234B") == False

def test_space():
    assert is_valid("SP ACE") == False
    assert is_valid("SPACE") == True

def test_punct():
    assert is_valid("AB.CD") == False
    assert is_valid("AB,CD") == False
