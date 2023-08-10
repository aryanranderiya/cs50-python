text = input("Input:")

vowel_list = ["a", "e", "i", "o", "u"]

for l in text:
    for _ in vowel_list:
        if l.lower() == _:
            l = ""

    print(l, end="")

print()
