import random

def main():
    generate_integer(get_level())

def get_level():

    while True :
        try :
            level = int(input("Level: "))
        except ValueError : continue
        print()

        if level > 3 or level < 1 : continue
        else : return level

def generate_integer(level):

    eee_counter = 0 ; correct_problems = 0

    if level == 1 :
        small_range = 0
        large_range = 9

    elif level == 2:
        small_range = 10
        large_range = 99

    elif level == 3:
        small_range = 100
        large_range = 999


    for _ in range(10) :
        a = random.randint(small_range,large_range)
        b = random.randint(small_range,large_range)
        while True :
            print (f"{a} + {b} =" , end="")
            c = a + b
            answer = int(input(""))

            if answer == c :
                correct_problems += 1
                break

            elif answer != c :
                eee_counter += 1

                if eee_counter >= 3 :
                    print(c)
                    break

                print("EEE")
                continue

        print(correct_problems)

if __name__ == "__main__":
    main()
