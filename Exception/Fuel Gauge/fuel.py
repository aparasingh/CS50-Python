def main():
    while True:
        x = get_fraction()
        if x > 1:
            pass
        else:
            percentage = int(round(x*100, 0))
            if percentage >= 99:
                print("F")
                return
            elif percentage <= 1:
                print("E")
                return
            else:
                print(f"{percentage}%")
                return


def get_fraction():
    while True:
        try:
            fraction = input("Fraction ")
            values = fraction.split("/")
            return int(values[0])/int(values[1])
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()
