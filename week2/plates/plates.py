def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    def check_numbers_letters() :

        numberindex = -1

        for c in s :
            if c.isnumeric() :
                numberindex = s.find(c)
                break

        if numberindex == -1 :
            return False
        else :

            for c in s[numberindex:len(s)]:
                if c.isalpha():
                    return True

    if "." in s or " " in s:
        return False
    elif s[0:2].isnumeric() :
        return False
    elif len(s) < 2 or len(s) > 6:
        return False
    elif s[0] =="0" :
        return False
    elif check_numbers_letters () :
        return False
    elif s[2] == "0" :
        return False
    else:
        return True

main()