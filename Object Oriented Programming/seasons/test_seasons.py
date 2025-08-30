from seasons import get_days,get_minutes,num_to_words
from datetime import date

def main():
    test_calcdays()
    test_calcmins()
    test_convert()


def test_calcdays():
    try:
        assert get_days("1324") == "Invalid date"
    except SystemExit:
        print("Invalid Date")
    assert get_days(str(date.today())) == 0

def test_calcmins():
    assert get_minutes(1) == 1440

def test_convert():
    assert num_to_words(1) == "one"



if __name__ == "__main__":
    main()
