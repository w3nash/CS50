from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar(-9)
    jar = Jar(7)
    assert jar.capacity == 7
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(11)


def test_withdraw():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(5)
    jar.withdraw(4)
    assert str(jar) == "🍪"
    jar.withdraw(1)
    assert str(jar) == ""
    with pytest.raises(ValueError):
        jar.withdraw(5)
