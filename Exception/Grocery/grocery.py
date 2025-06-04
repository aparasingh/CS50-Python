word_counts = {}

while True:
    try:
        word = input().strip()  # strip() to remove whitespace
        key = word.upper()
        word_counts[key] = word_counts.get(key, 0) + 1  # get the count of grocery item
    except EOFError:
        break

# Print sorted results
for key in sorted(word_counts.keys()):
    print(f"{word_counts[key]} {key}")
