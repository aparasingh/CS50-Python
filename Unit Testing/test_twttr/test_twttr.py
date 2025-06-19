from twttr import shorten


def main():
    test_capsletter()
    test_smallletter()
    test_number()
    test_character()


def test_capsletter():
    assert shorten("Apple") == "ppl"


def test_smallletter():
    assert shorten("apple") == "ppl"


def test_number():
    assert shorten("Apple1") == "ppl1"


def test_character():
    assert shorten("Apple.") == "ppl."


if __name__ == "__main__":
    main()
