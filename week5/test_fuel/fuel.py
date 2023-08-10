import sys
def main():
    print(gauge(convert(input("Fraction: "))))

def convert(fraction):
    # returns as percentage
    fraction = fraction.strip().split("/")
    while True:
        try:
            return round(int(fraction[0]) / int(fraction[1]), 2) * 100

        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def gauge(percentage):
    value = int(percentage)
    if 99 <= value <= 100:
        return("F")
    elif value <= 1:
        return("E")
    elif value > 100:
        main()
    else:
        return(str(value)+"%")


if __name__ == "__main__":
    main()
