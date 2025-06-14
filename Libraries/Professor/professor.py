from random import randint
from math import pow


def main():
    score = 0
    problems_counter = 10
    level = get_level()
    while problems_counter > 0:
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x + y
        try_counter = 3
        while try_counter > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == sum:
                    score = score + 1
                    problems_counter = problems_counter - 1
                    break
                else:
                    print("EEE")
                    if try_counter == 1:
                        problems_counter = problems_counter - 1
                    try_counter = try_counter - 1
                    pass
            except ValueError:
                if try_counter == 1:
                    problems_counter = problems_counter - 1
                try_counter = try_counter - 1
                pass
        print(f"{x} + {y} = {sum}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
            pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return randint(0, int(pow(10, level) - 1))
    else:
        return randint(int(pow(10, level-1)), int(pow(10, level) - 1))


if __name__ == "__main__":
    main()
