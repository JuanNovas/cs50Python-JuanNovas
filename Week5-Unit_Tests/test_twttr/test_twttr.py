from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("food") == "fd"
    assert shorten("twitter") == "twttr"
    assert shorten("HOuse") == "Hs"
    assert shorten("MY friend's name is PedrO") == "MY frnd's nm s Pdr"
    assert shorten("mi favourite number is 4") == "m fvrt nmbr s 4"
    assert shorten("hi, bye") == "h, by"
