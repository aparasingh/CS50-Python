import inflect
p = inflect.engine()
names = []
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print()
        break
print(f"Adieu, adieu, to {p.join(names, conj='and')}")
