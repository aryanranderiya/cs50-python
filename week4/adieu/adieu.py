# Commented code is code without using and importing external libraries (slightly incomplete)

# import sys
# name = []

# try :
#     while True :
#         name.append(input("Name: \n").capitalize())
#         print()

# except EOFError :

#     print("Adieu, adieu, to ", end="")
#     for i in range(len(name)-1) :
#         print(name[i] + ", ", end="")

#     if(len(name)>1) :
#         print("and", name[len(name)-1])
#     else :
#         print(name[0])

import inflect
p = inflect.engine()

name = [] ; mylist =[]

try :
    while True :
        name.append(input("Name: \n").capitalize())
        print()

except EOFError :

    mylist = p.join((name))

    print("Adieu, adieu, to ", end="")

    for i in range(len(mylist)) :
        print(mylist[i], end="")

    print()

# # JOIN WORDS INTO A LIST:

# mylist = p.join(("apple", "banana", "carrot"))
# # "apple, banana, and carrot"

# mylist = p.join(("apple", "banana"))
# # "apple and banana"

# mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# # "apple, banana and carrot"