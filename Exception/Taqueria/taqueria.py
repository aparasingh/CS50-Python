# Define menu as dictionary
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


amount = 0
while True:
    try:
        # Take order
        item = input("Item: ")
        # Convert provided input to title casing
        key = item.title()
        if key in menu:
            # Add up order amount
            amount = round(amount + menu[key], 2)
            # Print amount after every correct order
            print(f"${amount:.2f}")
    # Define exception on incorrect input
    except EOFError:
        break
    except ValueError:
        pass
# Add extra line at end of program
print()
