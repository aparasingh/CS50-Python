sum = 0
coin = 0
print("Amount Due: 50")
while sum < 50:
    while coin not in (10, 5, 25):
        if coin != 0:
            print("Amount Due: " + str(50 - sum))
        coin = int(input("Insert Coin: "))
    sum = sum + coin
    if sum < 50:
        print("Amount Due: "+ str(50 - sum))
    coin = 0
print("Change Owed: " + str(sum - 50))
