def take_input():
    while True:
        try:
            user_input = input("Fraction: ").strip().split("/")
            return round(int(user_input[0]) / int(user_input[1]), 2) * 100

        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def main():
    value = int(take_input())
    if 99 <= value <= 100:
        print("F")
    elif value <= 1:
        print("E")
    elif value > 100:
        take_input()
    else:
        print(int(value), "%", sep="")
