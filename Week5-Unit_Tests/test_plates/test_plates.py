from plates import is_valid

def test_is_valid():
    assert is_valid("cs50") == True
    assert is_valid("hi78") == True
    assert is_valid("12346") == False
    assert is_valid("8hi3") == False
    assert is_valid(".hi3") == False
    assert is_valid("cs05") == False
    assert is_valid("cs50p") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
