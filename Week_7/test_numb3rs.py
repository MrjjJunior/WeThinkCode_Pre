from numb3rs import validate


def test_valid():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("127.43.54.8") == True

def test_invalid():
    assert validate("256.23.54.7") == False
    assert validate("3245.332.456") == False
    assert validate("cat") == False

