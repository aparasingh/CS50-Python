def main():
    # Get Input on bill
    dollars = dollars_to_float(input("How much was the meal? "))
    # Get Input on tip percentage
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # Calculate tip
    tip = dollars * percent
    # Print tip output
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.split("$")[1])


def percent_to_float(p):
    return float(p.split("%")[0])/100


main()
