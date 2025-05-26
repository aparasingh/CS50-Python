def main():
    # Main function to get fuel fraction and share fuel gauge reading
    x = get_fraction()
    percentage = int(round(x*100))
    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")


def get_fraction():
    while True:
        try:
            fraction_input = input("Fraction ")
            numerator_str, denominator_str = fraction_input.split("/")
            numerator = int(numerator_str)
            denominator = int(denominator_str)
            fraction = numerator / denominator
            # Only return valid fractions (between 0 and 1)
            if 0 <= fraction <= 1:
                return fraction
            else:
                pass  # Re-prompt on incorrect value
        # Handle invalid input format or non-integer values
        except ValueError:
            pass
        except ZeroDivisionError:
            # Handle division by zero
            continue


main()
