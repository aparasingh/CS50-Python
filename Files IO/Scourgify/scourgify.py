import sys
from tabulate import tabulate

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    parts = sys.argv[1].split(".")
    if len(parts) == 2 and parts[1] == "csv":
        table = []
        try:
            with open(sys.argv[1], "r") as file:
                for line in file:
                    table.append(line.rstrip().split(","))
                print(tabulate(table, headers="firstrow", tablefmt="grid"))
                file.close()
            with open(sys.argv[2], 'w', newline='') as csvfile:
                fieldnames = ['first_name', 'last_name']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
                writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
                writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
                file.close()
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")
