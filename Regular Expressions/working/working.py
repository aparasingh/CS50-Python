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
            value = parts[0]
            time_of_day = parts[1]
            if re.search(r"[1-2][0-9]:[0-5][0-9]", value) or re.search(r"[1-9]:[0-5][0-9]", value):
                hours, minutes = value.split(':')
                if re.search(r"[0][1-9]", hours):
                    raise ValueError
            elif (re.search(r"[1-2][0-9]", value) or re.search(r"[1-9]", value)):
                try:
                    int(value) < 24
                    hours = value
                    minutes = '00'
                except ValueError:
                    raise ValueError
                if re.search(r"[0][1-9]", hours):
                    raise ValueError
            else:
                raise ValueError

            if time_of_day == 'PM' and hours != '12':
                hours = str(int(hours) + 12)
            elif time_of_day == 'PM' and hours == '12':
                hours = '12'
            elif time_of_day == 'AM' and hours == '12':
                hours = '00'

            times.append('{:02d}'.format(int(hours)) + ':' + minutes)
    except IndexError:
        raise ValueError

    return times[0] + ' to ' + times[1]


if __name__ == "__main__":
    main()
