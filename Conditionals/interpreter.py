expr = input("Expression: ")
x, y, z = expr.split(" ")
# Check if the sign is for addition
if (y == "+"):
    print(float(int(x) + int(z)))
# Check if the sign is for subtraction
elif (y == "-"):
    print(float(int(x) - int(z)))
# Check if the sign is for division
elif (y == "/"):
    print(float(int(x) / int(z)))
# Check if the sign is for multiplication
else:
    print(float(int(x) * int(z)))
