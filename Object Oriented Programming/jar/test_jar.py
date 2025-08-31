from jar import Jar


def main():
    test_init()
    test_str()
    test_deposit()


def test_init():
    jar = Jar()
    assert str(jar) == ""


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(4)
    assert True
    jar = Jar(10)
    try:
        jar.deposit(11)
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✓ Capacity exceeded test passed")


def test_withdraw():
    jar = Jar(10)
    jar.deposit(4)
    jar.withdraw(4)
    assert True
    jar = Jar(10)
    jar.deposit(10)
    try:
        jar.withdraw(11)
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✓ Capacity exceeded test passed")


if __name__ == "__main__":
    main()
