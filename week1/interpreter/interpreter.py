expression = input ("Expression:")

num1, op, num2 = expression.split(" ")

if op == "+":
    print (float(num1) + float(num2))

if op == "-":
    print (float(num1) - float(num2))

if op == "*":
    print (float(num1) * float(num2))

if op == "/":
    print (float(num1) / float(num2))