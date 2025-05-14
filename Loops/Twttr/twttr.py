post = input("Input: ")
for c in post:
    if c.lower() not in ('a', 'e', 'i', 'o', 'u'):
        print(c, end="")
print("")
