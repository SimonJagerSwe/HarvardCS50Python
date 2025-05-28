from twttr import shorten

def test_shorten_lower():
    assert shorten("education") == "dctn"

def test_shorten_upper():
    assert shorten("EDUCATION") == "DCTN"

def test_shorten_punctuation():
    assert shorten("Period. Comma,") != "Prd Cmm"

def test_shorten_ints():
    assert ("One 1 Two 2 Three 3") != "ne Tw hr"