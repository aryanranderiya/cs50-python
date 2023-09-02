import sys

if len(sys.argv) != 2 :
    sys.exit("Too many command line arguments!")

if not sys.argv[1].endswith(".py"):
    sys.exit("File must be a python file!")

linecounter = 0

try :
    with open(sys.argv[1]) as file :
        for line in file :
            if not line.strip().startswith("#") and line.strip():
                    linecounter += 1
except FileNotFoundError :
    sys.exit("File does not exist!")

print(linecounter)