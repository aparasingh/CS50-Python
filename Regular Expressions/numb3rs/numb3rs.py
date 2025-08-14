import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    values = ip.split('.')
    if len(values) == 4:
        try:
            for i in values:
                num = int(i)
                if num < 0 or num > 255:
                    return False
                elif re.search(r"^0", i) and num > 0:
                    return False
        except ValueError:
            return False
    else:
        return False

    return True


if __name__ == "__main__":
    main()
