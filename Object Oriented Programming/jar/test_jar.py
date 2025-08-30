from jar import Jar

def main():
    test_init()
    test_str()
    test_deposit()


def test_init():
    ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    ...



def test_withdraw():
    ...


if __name__ == "__main__":
    main()
