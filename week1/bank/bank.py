greeting = input("Input a Greeting for $$$:")

if greeting.lower().strip().startswith("hello"):
    print("$0")
elif greeting.lower().strip().startswith("h"):
    print("$20")
else:
    print("$100")
