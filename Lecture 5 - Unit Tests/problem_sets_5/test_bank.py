from bank import value

def test_value_hello():
   assert value("hello") == 0
   assert value("HELLO") == 0

def test_value_h_start():
    assert value("howdy, partner!") == 20
    assert value("HOWDY PARTNER!") == 20
    assert value("holy moly, it's you!") == 20
    assert value("HOLY MOLY, IT'S YOU!") == 20

def test_value_no_h():
    assert value("ah, there you are!") == 100
    assert value("AH, THERE YOU ARE!") == 100
    assert value("nice to see you, good sir!") == 100
    assert value("NICE TO SEE YOU, GOOD SIR") == 100
    assert value("oh no, not you again!") == 100
    assert value("OH NO, NOT YOU AGAIN") == 100
    assert value("what now?") == 100
    assert value("WHAT NOW?") == 100
