import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        times = []
        values = s.split(" to ")
        for i in range(2):
            time = values[i]
            if re.search(r"PM", time):
                parts = time.split(' ')
                value = int(parts[0]) + 12
                times.append(str(value) + ':00')
            else:
                parts = time.split(' ')
                times.append(str(parts[0]) + ':00')

    except IndexError:
        sys.exit(1)

    return times[0] + ' to ' + times[1]



if __name__ == "__main__":
    main()
