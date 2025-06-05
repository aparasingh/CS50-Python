months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        date_fin = date.strip()
        if ' ' in date_fin:
            fields = date_fin.split(" ")
            if len(fields) == 3 and len(date_fin.split(',')) == 2:
                month = months.index(fields[0]) + 1
                date = int(fields[1].split(',')[0])
                year = int(fields[2])
                if date < 32 and date > 0 and month >= 1 and month <= 12:
                    print(f"{year:04}-{month:02}-{date:02}")
                    break
        else:
            fields = date_fin.split("/")
            if len(fields) == 3:
                int_arr = [int(i) for i in fields]
                if int_arr[1] < 32 and int_arr[1] > 0 and int_arr[0] > 0 and int_arr[0] < 13:
                    print(f"{int_arr[2]:04}-{int_arr[0]:02}-{int_arr[1]:02}")
                    break
    except ValueError:
        pass
    except EOFError:
        break
    else:
        pass
