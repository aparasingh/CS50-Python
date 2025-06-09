import random

while True:
    try:
        level = int(input("Level: "))
        value = random.randint(1, level)
       # guess_int = int(guess_str)
        if level > 0:
            while True:
                try:
                    guess = int(input("Guess: "))
                    if value == guess:
                        print("Just right!")
                        break
                    elif guess < value:
                        print("Too small!")
                        pass
                    else:
                        print("Too large!")
                        pass
                except ValueError:
                    pass
        else:
            pass  # Silent reprompt
        break

    except ValueError:
        pass  # Silent reprompt
