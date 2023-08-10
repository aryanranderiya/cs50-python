def main():
    print(shorten(input("Input:")))


def shorten(word):
    final = ""
    vowel_list = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]

    if str(word).isnumeric():
        return word

    for l in word:
        for _ in vowel_list:
            if l == _:
                l = ""

        final += l

    return final


if __name__ == "__main__":
    main()
