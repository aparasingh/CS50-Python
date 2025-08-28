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
    try:
        birth_date = input("Date of Birth: ")
        return date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid date")

def get_days(birth_date):
    return abs(date.today() - birth_date).days

def get_minutes(days):
    return days * 24 * 60

def num_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)


if __name__ == "__main__":
    main()
