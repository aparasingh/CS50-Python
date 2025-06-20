def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s[0:2].isalpha() and s.isalnum():
            for c in s:
                if c.isnumeric():
                    if int(c) == 0:
                        return False
                    else:
                        part = s.split(c, 1)
                        if part[1].isnumeric():
                            return True
                        else:
                            return False
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
