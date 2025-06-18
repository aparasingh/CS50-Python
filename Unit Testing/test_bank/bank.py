def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    if (greeting.strip().lower().rfind("hello") == 0):
        return 0
    elif (greeting.strip().lower().rfind("h") == 0):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
