from twttr import shorten


def test_shorten_small():
    assert shorten("python") == "pythn"
    assert shorten("tshepiso") == "tshps"


def test_capital():
    assert shorten("Tshepiso") == "Tshps"


def test_numbers():
    assert shorten("1234") == "1234"
    assert shorten("-2") == "-2"
    assert shorten("0") == "0"


def test_special_char():
    assert shorten("T$hepis0") == "T$hps0"
