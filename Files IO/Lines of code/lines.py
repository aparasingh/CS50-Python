import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
else:
    parts = sys.argv[1].split(".")
    if len(parts) == 2 and parts[1] == "py":
        counter = 0
        with open(parts[0]+"/"+sys.argv[1], "r") as file:
            for line in file:
                counter = counter + 1
            print(counter)
    else:
        print("Not a Python file")

