from twttr import shorten

def test_twttr():
    assert shorten("Toshio") == "Tsh"
    assert shorten("casanova") == "csnv"
    assert shorten("12345") == "12345"
    assert shorten("UPPERCASE") == "PPRCS"
    assert shorten("Hello, World!") == "Hll, Wrld!"


if __name__ == "__main__":
    test_twttr()
