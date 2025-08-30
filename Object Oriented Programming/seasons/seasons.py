from datetime import date
import inflect
import sys


def main():
    birth_date = get_birthdate()
    days = get_days(birth_date)
    minutes = get_minutes(days)
    min_words = num_to_words(minutes)
    print(min_words.capitalize(), "minutes")


def get_birthdate():
    birth_date = input("Date of Birth: ")
    return birth_date


def get_days(birth_date):
    try:
        value = date.fromisoformat(birth_date)
        today = date.today()
        days = abs(today - value).days
        return days
    except ValueError:
        sys.exit("Invalid date")


def get_minutes(days):
    return days * 24 * 60


def num_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number, andword="")


if __name__ == "__main__":
    main()
