from datetime import date


def main():
    try:
        birth_date = input("Date of Birth: ")
        today = date.today()
        print(date.fromisoformat(birth_date))
    except ValueError:
        print("Invalid date")


if __name__ == "__main__":
    main()
