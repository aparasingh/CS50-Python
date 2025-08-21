import validators

value = input("What's your email address? ")
if value == '':
    print("Invalid")
elif validators.email(value):
    print("Valid")
else:
    print("Invalid")
