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
            if int(minutes) > 59:
                raise ValueError

            times.append('{:02d}'.format(int(hours)) + ':' + minutes)
    except IndexError:
        raise ValueError

    return times[0] + ' to ' + times[1]


if __name__ == "__main__":
    main()
