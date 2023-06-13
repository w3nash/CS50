from datetime import date
from seasons import convert, check_date


def test_check_date():
    assert check_date("1999-01-01") == (1999, 1, 1)
    assert check_date("January 1, 1999") == None


def test_convert():
    assert (
        convert(date(2000, 10, 26))
        == int((date.today() - date(2000, 10, 26)).days) * 24 * 60
    )
    assert (
        convert(date(1999, 1, 1))
        == int((date.today() - date(1999, 1, 1)).days) * 24 * 60
    )
