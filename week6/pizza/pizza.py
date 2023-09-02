import sys
import csv
from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

file_name = sys.argv[1]

if file_name == "sicilian.csv": type = "Sicilian Pizza"
elif file_name == "regular.csv": type = "Regular Pizza"


list = []

try:
    with open(file_name) as file:

        reader = csv.DictReader(file)

        list.append(reader.fieldnames)

        for row in reader:
            list.append([row[type], row["Small"], row["Large"]])

        print(tabulate(list, headers="firstrow",tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")