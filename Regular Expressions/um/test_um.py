from um import count


def main():
    test_withspaces()
    test_startofline()
    test_withchars()
    test_notmatch()


def test_withspaces():
    assert count("Hello um yes") == 1


def test_startofline():
    assert count("Um yes hello") == 1


def test_withchars():
    assert count("Um? what?") == 1


def test_notmatch():
    assert count("yum yum") == 0


if __name__ == "__main__":
    main()
