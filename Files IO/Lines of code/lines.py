import sys

default_path = '/workspaces/28184843/'
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    parts = sys.argv[1].split(".")
    if len(parts) == 2 and parts[1] == "py":
        counter = 0
        fileName = default_path + parts[0] + '/' + sys.argv[1]
        try:
            with open(fileName, "r") as file:
                for line in file:
                    if '#' not in line:
                        counter = counter + 1
                print(counter)
                file.close()
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")
