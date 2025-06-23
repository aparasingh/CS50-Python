import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
else:
    parts = sys.argv[1].split(".")
    if len(parts) == 2 and parts[1] == "py":
        file = open(sys.argv[1], "r")
        print(file)
    else:
        print("Not a Python file")

