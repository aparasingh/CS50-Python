from fuel import convert, gauge


def main():
    test_convertinvalid()
    test_convertvalid()
    test_percent()
    test_zerodiv()
    test_edge()


def test_convertinvalid():
    assert convert("cat/dog") == None
    assert convert("cat") == None
    assert convert("2") == None


def test_zerodiv():
    assert convert("2/0") == None


def test_convertvalid():
    assert convert("2/3") == 0.6666666666666666
    assert convert("3/3") == 1


def test_percent():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"


def test_edge():
    assert gauge(100) == "F"
    assert gauge(1) == "E"


if __name__ == "__main__":
    main()
