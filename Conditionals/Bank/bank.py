greeting = input("Greeting: ")
if (greeting.strip().lower().rfind("hello") == 0):
    print("$0")
elif (greeting.strip().lower().rfind("h") == 0):
    print("$20")
else:
    print("$100")
