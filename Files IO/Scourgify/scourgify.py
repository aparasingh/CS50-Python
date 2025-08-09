import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments")
else:åç
    try:
        with open(sys.argv[1], newline='') as readfile:
            reader = csv.DictReader(readfile)
            with open(sys.argv[2], 'w', newline='') as csvfile:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    name = row['name']
                    values = name.split(', ')
                    writer.writerow({'first': values[1], 'last': values[0], 'house': row['house']})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
