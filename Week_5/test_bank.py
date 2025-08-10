from bank import bank


def test_hello():
    assert bank("hello") == "$0"
    assert bank("Hello") == "$0"


def test_h():
    assert bank("how") == "$20"
    assert bank("hey") == "$20"
    assert bank("hi") == "$20"


def test_greetings():
    assert bank("greetings") == "$100"
    assert bank("Sup") == "$100"
    assert bank("ey") == "$100"
