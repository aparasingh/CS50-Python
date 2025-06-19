from bank import value


def main():
    test_hello()
    test_smallhello()
    test_h()
    test_smallh()
    test_greetings()
    test_smallgreet()


def test_hello():
    assert value("Hello") == 0


def test_smallhello():
    assert value("hello") == 0


def test_h():
    assert value("Hi") == 20


def test_smallh():
    assert value("hi") == 20


def test_smallgreet():
    assert value("greetings") == 100


def test_greetings():
    assert value("Greetings") == 100


if __name__ == "__main__":
    main()
