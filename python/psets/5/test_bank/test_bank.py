from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello, world") == 0
    assert value("HELLO") == 0


def test_h():
    assert value("hey") == 20
    assert value("hey, wazzup") == 20
    assert value("HEY") == 20


def test_else():
    assert value("What's up?") == 100
    assert value("yow") == 100
    assert value("YOW") == 100
