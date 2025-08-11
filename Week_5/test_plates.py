from plates import is_valid



def test_len():
    assert is_valid("QQ") == "Valid" 
    assert is_valid("GH77KK") == "Valid"
    assert is_valid("A") == "Invalid"
    assert is_valid("AXII367S") == "Invalid"

def test_startswith():
    assert is_valid("22") == "Invalid"
    assert is_valid("QL") == "Valid"

def test_small():
    assert is_valid("xl") == "Invalid"
    assert is_valid("aZUJI") == "Invalid"

