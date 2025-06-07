post = input("Input: ")
vowels = "aeiou"
result = ''.join(c for c in post if c.lower() not in vowels)
print(result)
