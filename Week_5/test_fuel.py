from fuel import fraction


def test_empty():
    assert fraction("0/1") == "E"
    assert fraction("1/100") == "E"


def test_full():
    assert fraction("1/1") == "F"
    assert fraction("99/100") == "F"


def test_percentage():
    assert fraction("1/2") == "50%"
    assert fraction("1/4") == "25%"
    assert fraction("3/4") == "75%"
