def main():
    while True:
        try:
            fraction_input = input("Fraction ")
            x = convert(fraction_input)
            if x != None:
                percentage = int(round(x*100))
                print(gauge(percentage))
                return
            else:
                pass
        except ValueError:
            pass


def convert(fraction):
    while True:
        try:
            numerator_str, denominator_str = fraction.split("/")
            numerator = int(numerator_str)
            denominator = int(denominator_str)
            fraction_float = numerator / denominator
            # Only return valid fractions (between 0 and 1)
            if 0 <= fraction_float <= 1:
                return fraction_float
            else:
                return  # Re-prompt on incorrect value
            # Handle invalid input format or non-integer values
        except ValueError:
            return
        except ZeroDivisionError:
            # Handle division by zero
            return


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
