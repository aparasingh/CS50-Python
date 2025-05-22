def main():
    # Get input of vanity plate number
    plate = input("Plate: ")
    # Check if plate is valid and print output
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Function definition to check if plate is valid
def is_valid(s):
    # check input text length
    if len(s) >= 2 and len(s) <= 6:
        # Check if value is alphanumeric and first two characters are alphabet
        if s[0:2].isalpha() and s.isalnum():
            # Find first number in value
            for c in s:
                # Check if character is numeric
                if c.isnumeric():
                    # Output if first number is 0
                    if int(c) == 0:
                        return False
                    # Validate whether all the characters afterwards are numbers
                    else:
                        part = s.split(c, 1)
                        if part[1].isnumeric():
                            return True
                        else:
                            # If all latter chars are not numbers
                            return False
            # Output if all characters are alphabets
            return True
        # Output if all characters are not alphabets
        else:
            return False
    # Output if length is smaller than 2 or greater than 6
    else:
        return False


main()