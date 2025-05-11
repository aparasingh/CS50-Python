print("Amount Due: 50")
coin = 0
while coin < 50:
    coin = int(input("Insert Coin: ")) + coin
print("Change Owed: " + str(coin - 50))
