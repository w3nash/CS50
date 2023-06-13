from um import count


def test_um():
    assert count("um") == 1
    assert count("yes") == 0


def test_um_symbol():
    assert count("um,") == 1


def test_um_cases():
    assert count("Um") == 1


def test_um_sentence():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
