dict = {}
while True:
    try:
        item = input()
        key = item.upper()
        if key in dict:
            dict[key] = dict[key] + 1
        else:
            dict.update({key: 1})
    except EOFError:
        break

myKeys = list(dict.keys())
myKeys.sort()

# Sorted Dictionary
sd = {i: dict[i] for i in myKeys}
for key, value in sd.items():
    print(f"{value} {key}")
