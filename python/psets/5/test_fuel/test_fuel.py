import pytest
from fuel import convert, gauge


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/cat")

def test_convert():
    assert convert("3/4") == 75
    assert convert("0/100") == 0
    assert convert("100/100") == 100


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
