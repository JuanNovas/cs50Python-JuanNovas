from um import count

def test_count():
    assert count("um") == 1
    assert count(" um ") == 1
    assert count("um Um UM tumum") == 3
