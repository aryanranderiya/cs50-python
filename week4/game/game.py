import random

while True :
    try:
        n = int(input("Level:"))
    except ValueError :
        continue

    if n <= 0 :
        continue
    else :
        number = random.randrange(1,n+1)
        break

while True:

    try:
        userguess = int(input("Guess:"))
    except ValueError :
        continue

    if userguess == number :
        print("Just right!")
        break
    elif userguess < number :
        print("Too small!")
        continue
    elif userguess > number :
        print("Too large!")
