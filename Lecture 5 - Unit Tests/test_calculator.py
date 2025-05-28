# Calculator test
import pytest

from calculator import square


# Main function for examples 1 & 2
# def main():
#     test_square()


# Example 1, too much code to be useful
'''def main():
def test_square():
    if square(2) != 4:
        print("2 squared was not 4")

    if square(3) != 9:
        print("3 squared was not 9")'''


# Example 2, using asserts, but requires a ton of code
'''def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")

    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")

    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")'''


# Example 3, adapted for pytest
'''def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    # assert square("cat") == ValueError    # For testing user input, not currently applicable'''


# Example 4
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

# if __name__ == "__main__":
#     main()