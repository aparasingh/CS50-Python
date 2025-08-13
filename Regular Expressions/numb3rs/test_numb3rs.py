from numb3rs import validate


def main():
    test_string()
    test_smallnum()
    test_bignum()
    test_invalid()


def test_string():
    assert validate("cat/dog") == False
    assert validate("cat") == False


def test_smallnum():
    assert validate("1.2.3.4") == True


def test_bignum():
    assert validate("255.255.255.255") == True


def test_invalid():
    assert validate("25") == False
    assert validate("509.1.2.3") == False
    assert validate("5.256.2.3") == False


if __name__ == "__main__":
    main()
