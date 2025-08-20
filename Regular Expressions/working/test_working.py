from working import convert


def main():
    test_withoutmins()
    test_withmins()
    test_withoutto()
    test_invalidtime()


def test_withoutmins():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_withmins():
    assert convert("9:05 AM to 5:10 PM") == "09:05 to 17:10"

def test_withoutto():
    try:
        assert convert("9 AM - 5 PM") == "9:00 - 17:00"
    except ValueError:
        print('Error scenario passed')

def test_invalidtime():
    try:
        assert convert("9:60 AM to 5 PM") == '09:60 to 17:00'
    except ValueError:
        print('Error scenario passed')


if __name__ == "__main__":
    main()
