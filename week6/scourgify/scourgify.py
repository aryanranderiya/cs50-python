import sys
import csv
from tabulate import tabulate

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

argument_one = sys.argv[1]
argument_two = sys.argv[2]

try:
    with open(argument_one) as file:
        reader = csv.DictReader(file)

        file = open(argument_two,"w")
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            house = row["house"]
            lastname, firstname = row["name"].split(",")
            writer.writerow(
                {
                    "first": firstname.strip(),
                    "last": lastname.strip(),
                    "house": house.strip(),
                }
            )

        file.close()
except FileNotFoundError:
    sys.exit("Could not read" + argument_one)
