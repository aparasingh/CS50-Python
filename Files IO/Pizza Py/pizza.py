import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
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
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")
