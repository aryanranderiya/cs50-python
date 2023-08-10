amount = 50
print("Amount due: ", amount)

while True:

    money = int(input("Insert Coin: "))

    if money == 25 or money==10 or money==5:
        amount = amount - money

    if amount <= 0:
            print("Change Owed:", abs(amount))
            break

    print("Amount Due:", amount)