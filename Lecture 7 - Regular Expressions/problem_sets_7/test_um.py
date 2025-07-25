from um_2 import count

def test_valid_single():
    # assert count("Oooooh-la-la") == 0
    assert count("Um... what's all of this, then?") == 1
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_valid_double():
    assert count("Um... so... what are we... um.. doing?") == 2
    assert count("um, thanks, um, regular expressions make sense now") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

def test_valid_triple():
    assert count("Umm, um, Um, umm, what? UM?") == 3

def test_invalid_input():
    assert count("Um... yum... tum...")  != 3
    assert count("Um Yummy in my umm... TUMMY") == 1
