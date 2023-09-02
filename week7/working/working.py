import re
import sys


def main():

    print(convert(input("Hours: ").strip()))

def convert(s):

    if match := re.search(r"(\d?\d):?(\d\d)? (AM|PM) to (\d?\d):?(\d\d)? (PM|AM)", s, re.IGNORECASE) :

        hour1=int(match.group(1))
        ampm1=match.group(3)

        hour2=int(match.group(4))
        ampm2=match.group(6)

        try :
            minute1=int(match.group(2))
            minute2=int(match.group(5))
        except TypeError :
            minute1 = 0
            minute2 = 0

        if minute2 or minute1 >= 60 :
            raise ValueError

        if ampm1 == "PM" :
            if hour1 == 12 :
                hour1 = 12
            else :
                hour1 = int(hour2)+12
        else : # if AM
            if hour1 == 12 :
                hour1 = 0

        if ampm2 == "PM" :
            if hour2 == 12 :
                hour2 = 12
            else :
                hour2 = int(hour2)+12
        else : #if AM
            if hour2 == 12 :
                hour2 = 0

        return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"

    else :
        raise ValueError

if __name__ == "__main__":
    main()