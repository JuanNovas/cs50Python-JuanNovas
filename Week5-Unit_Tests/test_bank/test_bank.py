from bank import value

def test_value():
    assert value("hello") == 0
    assert value("hello Jhon") == 0
    assert value("HeLLo bro") == 0
    assert value("Hi dude") == 20
    assert value("hell mother") == 20
    assert value("") == 100
    assert value("you again?") == 100
    assert value(",ello") == 100
