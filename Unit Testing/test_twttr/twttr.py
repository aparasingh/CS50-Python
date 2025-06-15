def main():
    post = input("Input: ")
    print(shorten(post))


def shorten(word):
    vowels = "aeiou"
    return ''.join(c for c in word if c.lower() not in vowels)


if __name__ == "__main__":
    main()
