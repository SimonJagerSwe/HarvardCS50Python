import random
from numb3rs import validate

# Test hard coded, valid IP
def test_valid_hard():
    assert validate("127.0.0.1") == True


# Test randomised IP in valid range
def test_valid_random():
    valid_list = []
    for i in range(4):
        valid_list.append(str(random.randint(0,255)))
    delimiter = "."
    assert validate(delimiter.join(valid_list)) == True


# Test non-numeral
def test_non_numeral():
    assert validate("cat") == False


# Test a hard coded, too short IP
def test_too_few_hard():
    assert validate("1.2.3") == False


# Test a randomised too short IP
# Excessively verbose
def test_too_few_random():
    short_list = []
    for i in range(3):
        i = random.randint(0,255)
        i = str(i)
        short_list.append(i)
    delimiter = "."
    three_ip = delimiter.join(short_list)
    assert validate(three_ip) == False


# Test a hard coded, too long IP
def test_too_many_hard():
    assert validate("1.2.3.4.5") == False


# Test a randomised too long IP
# Pretty clear
def test_too_many_random():
    long_list = []
    for i in range(5):
        i = str(random.randint(0,255))
        long_list.append(i)
    delimiter = "."
    five_ip = delimiter.join(long_list)
    assert validate(five_ip) == False


# Test an IP featuring hard coded negative numbers
def test_negative_hard():
    assert validate("1.2.3.-1") == False


# Test an IP featuring randomly generated negative numbers
# Excessively chonky way of appending
def test_negative_random():
    negative_list = []
    for i in range(4):
        negative_list.append(str(random.randint(-255, -1)))
    delimiter = "."
    negative_ip = delimiter.join(negative_list)
    assert validate(negative_ip) == False


# Test an IP with hard coded numbers exceeding 255
def test_too_high_hard():
    assert validate("256.1000.1987.512") == False


# Test an IP with randomised numbers exceeding 255
# Nice and short
def test_too_high_random():
    high_list = []
    for i in range(4):
        high_list.append(str(random.randint(256, 10000)))
    delimiter = "."
    assert validate(delimiter.join(high_list)) == False


# Test valid first numer, invalid second
def test_valid_first_hard():
    assert validate("127.456.0.1") == False
