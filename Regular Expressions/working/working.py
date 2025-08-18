import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        times = []
        values = s.split(" to ")
        for i in range(2):
            parts = values[i].split(' ')
            time = parts[0]
            time_of_day = parts[1]
            if re.search(r":", time):
                hours, minutes = time.split(':')
            else:
                hours = time
                minutes = '00'
            if time_of_day == 'PM':
                hours = str(int(hours) + 12)
            times.append(hours + ':' + minutes)
    except IndexError:
        sys.exit(1)

    return times[0] + ' to ' + times[1]


if __name__ == "__main__":
    main()
