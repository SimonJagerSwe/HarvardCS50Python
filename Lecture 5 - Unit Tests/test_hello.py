from hello import hello

def test_hello():
    hello("David") == "Hello, David"

def test_argument():
    assert hello() == "Hello, world"