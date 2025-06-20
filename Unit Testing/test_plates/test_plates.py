from plates import is_valid


def main():
    test_invalidlength()
    test_invalidnum()
    test_valid()
    test_invalidchars()


def test_invalidlength():
    assert is_valid("OUTATIME") == False
    assert is_valid("A") == False


def test_invalidnum():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("50CS") == False


def test_valid():
    assert is_valid("CS50") == True


def test_invalidchars():
    assert is_valid("PI3.14") == False
    assert is_valid("P314") == False


if __name__ == "__main__":
    main()
