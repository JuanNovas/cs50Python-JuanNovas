from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("2/4") == 50
    assert convert("3/3") == 100
    assert convert("0/2") == 0
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("2/cat")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(78) == "78%"
    assert gauge(-10) == "E"
    assert gauge(990) == "F"
