import random
import math

def main():
    score = 0
    problems_counter = 10
    level = get_level()
    x = generate_integer(level)
    y = generate_integer(level)
    sum = x + y
    while True:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == sum:
                score = score + 1
            else:



        except ValueError:
            pass

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1,2,3):
                return level
            pass
        except ValueError:
            pass


def generate_integer(level):

    return random.randint(math.pow(10,level-1), math.pow(10,level) - 1)


if __name__ == "__main__":
    main()
