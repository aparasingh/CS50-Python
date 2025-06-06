months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date_input = input("Date: ").strip()

        if ',' in date_input:  # Month DD, YYYY format
            parts = date_input.split()
            if len(parts) == 3 and parts[1].endswith(','):
                month_name = parts[0]
                day = int(parts[1][:-1])  # Remove comma
                year = int(parts[2])

                if month_name in months:
                    month = months.index(month_name) + 1
                    if 1 <= day <= 31 and 1 <= month <= 12:
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break

        elif '/' in date_input:  # MM/DD/YYYY format
            parts = date_input.split('/')
            if len(parts) == 3:
                month, day, year = map(int, parts)
                if 1 <= day <= 31 and 1 <= month <= 12:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break

        pass  # Silent reprompt

    except (ValueError, IndexError):
        pass  # Silent reprompt
    except (EOFError, KeyboardInterrupt):
        break
