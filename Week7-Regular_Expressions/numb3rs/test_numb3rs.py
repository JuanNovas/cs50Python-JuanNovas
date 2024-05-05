from numb3rs import validate

def test_validate():
    assert validate("0.0.0.0") == True
    assert validate("256.256.256.256") == False
    assert validate("01.256.256.256") == False
    assert validate("255.255.255.255") == True


