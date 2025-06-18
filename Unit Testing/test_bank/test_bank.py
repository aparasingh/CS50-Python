from bank import value


def main():
    test_value()


def test_value():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hi") == 20
    assert value("hi") == 20
    assert value("greetings") == 100
    assert value("Greetings") == 100


if __name__ == "__main__":
    main()
