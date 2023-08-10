groceriesdict = {}

while True :

    try :
        key = input("")

        if key in groceriesdict : groceriesdict[key] += 1
        else : groceriesdict[key] = 1

    except EOFError :
        for k in sorted(groceriesdict) :
            print (groceriesdict[k], k.upper(), sep=" " , end="\n")
        break

    except KeyError : pass
