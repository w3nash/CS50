from plates import is_valid


def test_beginning():
    assert is_valid("50CS") == False
    assert is_valid("CS50") == True


def test_length():
    assert is_valid("1") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("AA") == True


def test_middle():
    assert is_valid("ABC12D") == False


def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("CCC001") == False
    assert is_valid("CS50") == True


def test_alpha():
    assert is_valid("NRVOUS") == True
    assert is_valid("123123") == False


def test_alphanum():
    assert is_valid("PI3.14") == False