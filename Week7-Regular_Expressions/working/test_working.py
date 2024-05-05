from working import convert
import pytest

def test_convert():
    assert convert("12 AM to 4 PM") == "00:00 to 16:00"
    with pytest.raises(ValueError):
        convert("5 AM 9 PM")
    with pytest.raises(ValueError):
        convert("18 AM to 9 PM")
