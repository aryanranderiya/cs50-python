name = input("Enter your name: ")

for letter in name:

    if letter.isupper() : letter = "_" + letter

    print (letter.lower(), end="")

print()

