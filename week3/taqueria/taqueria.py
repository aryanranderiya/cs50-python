menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

flag = True ; ordertotal = []

def takeuserinput() :

    try :
        order = input("Item:").title()
        if order in menu : ordertotal.append(round(menu[order],3))
        return True

    except EOFError :
        return False
    except KeyError : return False


while flag :
    flag = takeuserinput()
    if not flag :
        break
    print (f"${sum(ordertotal):.2f}")
    print()

